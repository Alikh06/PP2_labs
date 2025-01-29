#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
// Задача A: 72477. Oddlover
// Given an array consisting of integers. 
// Write a program, which outputs all odd 
// elements of array.
int main(){
    int a;
    cin >> a;
    int n[a];
    for(int i = 0; i < a; i++){
        cin >> n[i];
        if(n[i] % 2 != 0) {
            cout << n[i] << " ";
        }
    }
    return 0;
}

// Задача B: 72485. Positive numbers
// Given an array consisting of integers. 
// Write a program, which outputs count of 
// positive numbers in array.
int main(){
    int a;
    cin >> a;
    int n[a];
    int count = 0;
    for(int i = 0; i < a; i++){
        cin >> n[i];
        if( n[i] > 0){
            count ++;
        }
    }
    cout << count;
    return 0;
}

// Задача C: 72568. Maxmimum in array
// Given an array consisting of integers. 
// Write a program, which outputs maximum in array.
int main(){
    int a;
    cin >> a;
    int n[a];
    for(int i = 0; i < a; i++){
        cin >> n[i];
    }
    int maxx = n[0];
    for(int i = 1; i < a; i++){
        if(maxx < n[i]){
            maxx = n[i];
        }
    }
    cout << maxx;
    return 0;
}

// Задача D: 72569. Position of maximum
// Given an array consisting of integers. 
// Write a program, which finds position of 
// maximum element of array. If maximums is 
// two or more you should output first position.
int main(){
    int a;
    cin >> a;
    int n[a];
    int b = 1;
    for(int i = 0; i < a; i++){
        cin >> n[i];
    }
    int maxx = n[0];
    for(int i = 1; i < a; i++){
        if(maxx < n[i]){
            maxx = n[i];
            b = i + 1;
        }
    }
    cout << b;
    return 0;
}

// Задача E: 386467. Alphabet
// You’re given an ordinal number 
//  representing a letter of the English alphabet. 
//  Output what uppercase and lowercase letters 
//  corresponds with this number. If there is no 
//  such letter in the English alphabet, print No 
//  such letter!
int main(){
    int a;
    cin >> a;
    if(a >= 1 && a <= 26){
        char uppercase = 'A' + (a - 1);
        char lowercase = 'a' + (a - 1);
        cout << uppercase << " " << lowercase;
    }
    else {
        cout << "No such letter!";
    }
    return 0;
}

// Задача F: 105006. A or a
// Hi! I have just remembered a very interesting problem. 
// It is a very easy task and I hope that everyone will 
// be able to cope with it! You need to make small letters 
// big, and vice versa. Good luck everyone!
int main(){
    char a;
    cin >> a;
    if(islower(a)) {
        cout << char(toupper(a));
    }
    else {
        cout << char(tolower(a));
    }
    return 0;
}

// Задача G: 72763. Sum of array
// Given an array consisting of integers. 
// Write a program, which finds sum of all elements.
int main(){
    int a;
    cin >> a;
    long array[a];
    long sum = 0;
    for (int i = 0; i < a; i++){
        cin >> array[i];
        sum += array[i];
    }
    cout << sum;
    return 0;
}

// Задача H: 72768. Reverse
// Given an array consisting of integers. 
// Print all array in reverse order.
int main(){
    int a;
    cin >> a;
    int array[a];
    for (int i = 0; i < a; i++){
        cin >> array[i];
    }
    for (int i = a-1; i >= 0; i--){
        cout << array[i] << " ";
    }
    return 0;
}

// Задача I: 72780. MaxToMin
// Given an array consisting of integers. 
// Write a program, which will change all maximal 
// elements to minimal elements of the array. 
// Look to sample to better understand the conditions.
int main(){
    int a;
    cin >> a;
    int array[a];
    for (int i = 0; i < a; i++){
        cin >> array[i];
    }


    int min = array[0], max = array[0];
    for(int i = 1; i < a; i++){
        if(min > array[i]){
            min = array[i];
        }
        if(max < array[i]){
            max = array[i];
        }
    }
    for(int i = 0; i < a; i++){
        if(array[i] == max){
            array[i] = min;
        }
    }
    
    for(int i = 0; i < a; i++){
        cout << array[i] << " ";
    }
    return 0;
}

// Задача J: 72783. Sum l...r
// Given an array consisting of integers. 
// Write program, which will get sum of elements a[i], 
// where i(l <= i <= r)
int main(){
    int n, l, r;
    cin >> n >> l >> r;
    vector<int> array(n);
    for(int i = 0; i < n; i++){
        cin >> array[i];
    }
    long long result_sum = 0;
    for( int i = l - 1; i < r; i++){
        result_sum += array[i];
    }
    cout << result_sum;
    return 0;
}

// Задача K: 72871. Reverse elements on l...r
// Given an array consisting of integers. 
// Write program, which will reverse elements in interval 
int main(){
    int n, l, r;
    cin >> n >> l >> r;
    vector<int> array(n);
    for(int i = 0; i < n; i++){
        cin >> array[i];
    }
    reverse(array.begin() + (l - 1), array.begin() + r);
    for( int i = 0; i < n; i++){
        cout << array[i] << " ";
    }
    return 0;
}

// Задача L: 73239. Upper bound -1?
// Given a sorted array and a target value, 
// return the index if the target is found. 
// If not, return the index where it would be 
// if it were inserted in order.
// You may assume no duplicates in the array.
int main() {
    int a, b;
    cin >> a >> b;
    vector<int> nums(a);

    for(int i = 0; i < a; i++){
        cin >> nums[i];
    }

    int index = 0;
    while( index < a && nums[index] < b) {
        index++;
    }
    cout << index;
    return 0;
}

// Задача R: 73266. Sort
// Given an array. Sort it. And reverse it.
int main() {
    int a;
    cin >> a;
    vector<int> arr(a);
    for(int i = 0; i < a; i++){
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    reverse(arr.begin(), arr.end());
    for( int i = 0; i < a; i++){
        cout << arr[i] << " ";
    }
    return 0;
}

// Задача M: 73242. Duplicates
// Given a sorted array, write a program 
// which will delete all duplicates of elements 
// and just save one of them.

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    sort(nums.begin(), nums.end());

    auto last = unique(nums.begin(), nums.end());

    nums.erase(last, nums.end());

    for (const int& num : nums) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}

// Задача W: 386458. Dec to Hex.
// Given a decimal number 
// , convert it to hexadecimal numeric system. 
// It is guaranteed that 4 hexadecimal digits will be 
// enough to represent the number 
// Hexadecimal numbers use 16 values to represent a number. 
// The numbers 0 through 9 are represented by the characters 
// 0-9, and 10-15 are represented by the characters 
// A through F.
int main() {
    int n;
    cin >> n;
    char hex[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
    string result;;
     if (n == 0) {
        result = "0"; 
        } 
    else {
        while (n > 0) {
            result = hex[n % 16] + result; 
            n /= 16;
        }
    }
    cout << result;
    return 0;
}




