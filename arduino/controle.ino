# include < PETEletrica .h >

// funcao do filtro de kalman
 double KALMAN ( double U){
 static const double R = 40; // covariancia do ruido
 static const double H = 1.00; // mapa de medicao escalar
 static double Q = 10; // covariancia estimada inicial
 static double P = 0; // erro covariancia inicial
 static double U_hat = 15; // estado estimado inicial
 static double K = 0; // ganho de kalman inicial

 K = P*H /( H*P*H+R);
 U_hat = U_hat + K *(U -H* U_hat );

 P = (1 - K*H)*P+Q;

 return U_hat ;
 }

 double filtrado ;
 int trigger = 3, echo = 2;
 int IN1 = 4, IN2 = 5, IN3 = 6, IN4 = 7;
 float d = 0;
 SensorUltrassonico ultrassonico ( trigger , echo );
 Motores motor ( IN1 , IN2 , IN3 , IN4 );

 void setup () {
 Serial . begin (9600) ;
 }

 void loop () {

 long microsec = ultrassonico . timing () ;
 d = ultrassonico . convert ( microsec , SensorUltrassonico :: CM );
 delay (10) ;

 Serial . print (" Distancia : ");// usando so de comparacao
 Serial . print (d);// usando so de comparacao
 Serial . print (" / ");
 filtrado = KALMAN (d);// chama a funcao do filtro
 Serial . print (" Filtrados : ");// indica a saida filtrada
 Serial . println ( filtrado );// printa a saida filtrada

 delay (250) ;
 motor . set_motors (0 , 1000) ;

 while (d < 5 || d > 18) {
 long microsec = ultrassonico . timing () ;
 d = ultrassonico . convert ( microsec , SensorUltrassonico :: CM );
 delay (10) ;

 Serial . print (" Distancia : ");// usando so de comparacao
 Serial . print (d);// usando so de comparacao
 Serial . print (" / ");
 filtrado = KALMAN (d);// chama a funcao do filtro
 Serial . print (" Filtrados : ");// indica a saida filtrada
 Serial . println ( filtrado );// printa a saida filtrada
 delay (250) ;
motor . set_motors (0 , 0) ;
 }
 }
