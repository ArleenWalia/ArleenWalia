//Aqua Carwash prototype
#include<avr/io.h>
#include<util/delay.h>
#define setbit(x,y)(x|=y)
#define clearbit(x,y)(x&=~y)
#define checkbit(x,y)((x)&(y))
#define bitn(p)(0x01<<(p))
int main(void)
{
  DDRD = 0xFF;
  DDRB = 0xFF;
  int brush1;
  int brush2;
  int conveyor;
  while (1)
  {
    ADMUX = 0x40;     //Connect IR sensor to PortA Pin0
    ADCSRA = 0xC7; 
    while(checkbit(ADCSRA,bitn(ADSC)));
    ADCW = brush1;    //Set the finished converted data to the 'brush 1' variable

    ADMUX = 0x41;     //connect IR sensor to PortA Pin1
    ADCSRA = 0xC7; 
    while(checkbit(ADCSRA,bitn(ADSC)));
    ADCW = brush2;    //Set the finished converted date to the 'brush 2' variable
    
    ADMUX = 0x42;     //connect IR sensor to PortA Pin2
    ADCSRA = 0xC7; 
    while(checkbit(ADCSRA,bitn(ADSC)));
    ADCW = conveyor;    //Set the finished converted date to the 'conveyor' variable

    if(brush1<50)
    {
      setbit(PORTB,bitn(4)); // Motor for Brush 1
      clearbit(PORTB,bitn(5));
      _delay_ms(100);
    }
    else
    {
      clearbit(PORTB,bitn(4));
      clearbit(PORTB,bitn(5));
      _delay_ms(100);
    }

    if(brush2<50)
    {
      setbit(PORTD,bitn(4)); // Motor for Brush 2
      clearbit(PORTD,bitn(5));
      setbit(PORTB,bitn(0)); // RGB Light
      _delay_ms(100);
    }
    else
    {
      clearbit(PORTD,bitn(4));
      clearbit(PORTD,bitn(5));
      clearbit(PORTB,bitn(0));
      _delay_ms(100);
    }

    setbit(PORTD,bitn(6)); // Motor for Conveyor
    clearbit(PORTD,bitn(7));
    _delay_ms(100);
  }
}