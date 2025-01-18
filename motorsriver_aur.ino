// Pin definitions
const int IN1 = 2;
const int IN2 = 3;
const int IN3 = 4;
const int IN4 = 5;

// Initialize GPIO pins
void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  Serial.begin(9600);
}

// Move forward
void forward(int sec) {
  Serial.println("Moving forward");
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(sec * 1000);
}

// Move reverse
void reverse(int sec) {
  Serial.println("Moving reverse");
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  delay(sec * 1000);
}

// Turn left
void left(int sec) {
  Serial.println("Turning left");
  digitalWrite(IN1, LOW);  // Stop or reverse left motor
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH); // Move right motor forward
  digitalWrite(IN4, LOW);
  delay(sec * 1000);
}

// Turn right
void right(int sec) {
  Serial.println("Turning right");
  digitalWrite(IN1, HIGH); // Move left motor forward
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);  // Stop or reverse right motor
  digitalWrite(IN4, LOW);
  delay(sec * 1000);
}

// Main program
void loop() {
  Serial.println("Starting motor test");
  forward(2);  // Move forward for 2 seconds
  left(1);     // Turn left for 1 second
  forward(2);  // Move forward for 2 seconds
  right(1);    // Turn right for 1 second
  reverse(2);  // Move backward for 2 seconds

  // Add a delay before the next iteration
  delay(10000); // 10 seconds
}
