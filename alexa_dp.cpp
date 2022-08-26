#include<iostream>
#include<vector>
using namespace std;
struct alexa{
    int m_stocks;
    vector<int> stocks;
};
int main(){
    int n;
    vector<alexa> procesos;
    cin >> n;
    for(int i = 0; i < n; i++){
        alexa nueva;
        int a;
        cin >> a;
        nueva.m_stocks = a;
        for(int i = 0; i < a; i++){
            int b;
            cin >> b;
            nueva.stocks.push_back(b);
        }
        procesos.push_back(nueva);
    }
    for(int i = 0; i< n; i++){
        alexa actual = procesos[i];
        for(int i = 0; i < actual.m_stocks;i++){
            
        } 
    }
}