#include <iostream>
#include <cmath>
using namespace std;
// Задача B: 78567 Almaz's work
// Almaz dug up h miters of hollow in m hours. How many meters will Almaz dig up in t hours
// int main() {
//     setlocale (LC_ALL, "RU");
//     float h;
//     float m;
//     float t;
//     cin >> h;
//     cin >> m;
//     cin >> t;
//     cout << (h / m) * t;
//     return 0;
// }


// Задача D: 78571 Change char
// Given character ch. Increase ascii code of this character by 14 and print new character.
// int main() {
//     setlocale(LC_ALL, "RU");
    
//     char ch;
//     cin >> ch;
//     char new_ch = ch + 14;
//     cout <<new_ch << endl;
    
//     return 0;
// }


// Задача E: 78564 Clock
// Given how many hours the clock shows. Find the angle between the clock’s hours arrow and 12 modulo 180.
// int main() {
//     setlocale(LC_ALL, "RU");
//     int h;
//     int d = 30;
//     cin >> h;
//     cout << (h * d) % 180;
//     return 0;
// }


// Задача F: 78667 Hunter
// Hunter on the first i = 1 day of the hunt met n rabbits. 
// Every next i-th day he met 2 * i times more rabbits than
// on first day. Find how much in total rabbits he met in d
// days of hunting
// int main(){
//     int n, d;
//     int total_rabits = 0;
//     cin >> n >> d;
//     for (int i = 1; i <= d; ++i) {
//         if (i == 1) {
//             total_rabits += n;
//         }
//         else {
//             total_rabits += 2*i*n;
//         }
//     }
//     cout << total_rabits;
//     return 0;
// }


// Задача G: 78583 Investor's money
// Investor invested t tg into start-up. 
// Every month his investments doubles. 
// Find how much will be his investments after n month.
// int main() {
//     int t, n , c;
//     cin >> t >> n;
//     int total = t;
//     for (int i = 1; i <= n ; i++) {
//         c = t * 2;
//         total += c;
//         t = c;
//     }
//     cout << total;
//     return 0;
// }


// Задача H: 78556 Programing language
// Given number of n students in class who knows c++,
// number of m students who knows python and total number 
// of t students in the class. Find how many students knows
// both programing languages if there is no student in class 
// who don’t know any of this two languages.
// int main() {
//     int n,m,t;
//     cin >> n >> m >> t;
//     cout << t - (t-n) - (t-m);
//     return 0;
// }


// Задача I: 51191. Root
// You are given integer number.
// Print out its square root value.
// int main() {
//     double a;
//     cin >> a;
//     cout << sqrt(a);
//     return 0;
// }


// Задача J: 78608 Area of triangle
// Given sides of triangle. Find area of triangle.
// int main() {
//     int a,b,c;
//     cin >> a >> b >> c;
//     double P = a+b+c;
//     double p = P/2;
//     double S = sqrt(p*(p-a)*(p-b)*(p-c));
//     printf("%.2f" , abs(S));
//     return 0;
// }