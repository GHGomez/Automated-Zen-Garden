#include <Servo.h>

#define S1_PIN 5
#define S2_PIN 6

Servo s1, s2;

float demo_set[][2] = {
  {90, 0},
  {124, 20},
  {85, 46},
  {102, 64},
  {138, 46},
  {124, 20}
};

int curr = 0;

void setup() {
  Serial.begin(9600);
  s1.attach(S1_PIN);
  s2.attach(S2_PIN);

  s1.write(85);
  s2.write(5);
  delay(1000);

//  demo();
}

void demo() {
  for (int i = 0; i < 4; i++) {
    s1.write(demo_set[i][0]);
    s2.write(demo_set[i][1]);
    delay(1000);
  }
}

void loop() {
  if (curr < 6) {
    int same = 0;
    if (demo_set[curr][0] != demo_set[curr + 1][0]) {
      s1.write(demo_set[curr][0]);
      if (demo_set[curr][0] < demo_set[curr + 1][0]) {
        demo_set[curr][0]++;
      } else {
         demo_set[curr][0]--;
      }
    } else {
      same++;
    }
    if (demo_set[curr][1] != demo_set[curr + 1][1]) {
      s2.write(demo_set[curr][1]);
      if (demo_set[curr][1] < demo_set[curr + 1][1]) {
        demo_set[curr][1]++;
      } else {
        demo_set[curr][1]--;
      }
    } else {
      same++;
    }
    if (same > 1) {
      curr++;
    }
    delay(100);
  }
}
