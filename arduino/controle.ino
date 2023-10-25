include < PETEletrica .h >

//kalman filtro
double KALMAN(double U){
  static const double R = 40;//noise covariance
  static const double H = 1.00;//measurement map scalar
  static double Q = 10;//initial estimated covariance
  static double P = 0;//initial error covariance
  static double U_hat = 15;//initial estimated state
  static double K = 0;//initial kalman gain

  K = P*H/(H*P*H+R);
  U_hat = U_hat + K*(U-H*U_hat);

  P = (1-K*H)*P+Q;

  return U_hat;
}

double filtrado;

int trigger = 3, echo = 2;
int IN1 = 4, IN2 = 5, IN3 = 6, IN4 = 7;
float d = 0;
SensorUltrassonico ultrassonico(trigger, echo);
Motores motor(IN1, IN2, IN3, IN4);

void setup() {
 Serial.begin(9600); 
 }

void loop() {

  long microsec = ultrassonico.timing();
  d = ultrassonico.convert(microsec, SensorUltrassonico::CM);
  delay(10);
  
  Serial.print("Distância: ");//usando só de comparação
  Serial.print(d);//usando só de comparação
  Serial.print(" / ");
  filtrado = KALMAN(d);//chama a função do filtro
  Serial.print("Filtrados: ");//indica a saída filtrada
  Serial.println(filtrado);//printa a saída filtrada

  delay(250); 
  motor.set_motors(0, 100);

  

while (d < 5 ||  d > 18) {
  long microsec = ultrassonico.timing();
  d = ultrassonico.convert(microsec, SensorUltrassonico::CM);
  delay(10);

  Serial.print("Distância: ");//usando só de comparação
  Serial.print(d);//usando só de comparação
  Serial.print(" / ");
  filtrado = KALMAN(d);//chama a função do filtro
  Serial.print("Filtrados: ");//indica a saída filtrada
  Serial.println(filtrado);//printa a saída filtrada

  delay(250); 
  motor.set_motors(0, 0);
}
}
