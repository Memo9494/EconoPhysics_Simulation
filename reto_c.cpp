#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<utility>
#include<cmath>
using namespace std;

struct clase{
    int np;
    int min;
    int max;
};

bool ord(int a, int b){
    return a < b;
}

vector<int> distribucion_delta(vector<int> personas, int max, int n_personas){
    for(int i = 0; i < n_personas ; i++){
        personas.push_back(max/n_personas);
    }
    return personas;
}

vector<int> distribucion_uniforme(vector<int> personas, int max, int n_personas){
    for(int i = 0; i < n_personas ; i++){
        personas.push_back(max/n_personas);
    }
    return personas;
}

vector<int> intercambio(vector<int> personas, int interacciones, int n_personas){
    for(int i = 0; i < interacciones; i++){
        int l = rand()%100;
        int r = rand()%100;
        int pond = 1;
        int random = rand()%2;
        int cambio;
        if(random == 0){
            cambio = -pond;
        }
        else{
            cambio = pond;
        }
        if((personas[l] + cambio) > 0 && (personas[r] - cambio) > 0){
            personas[l] = personas[l] + cambio;
            personas[r] = personas[r] - cambio;
        }
        
    }
    return personas;
}

vector<clase> haz_clases(vector<int> intercambio_entre_personas, vector<clase> clases){
    int j = 0;
    for(int i = 0; i < intercambio_entre_personas.size();i++){
        if(j == 4){
            clases[j].np += 1;
        }
        else if(intercambio_entre_personas[i] < clases[j].max){
            clases[j].np += 1;
        }
        else{
            j = j+1;
        }
    }
    
    for(int i = 0; i < clases.size();i++){
        cout << clases[i].min << ' ' << clases[i].max << ' ' << clases[i].np << endl;
    }
    cout << endl;
    return clases;
}
// void print_n_moments(int clases, int n, vector<int> personas){
//     if(n == 0){
//         return;
//     }
//     else{
//         vector<clase> nuevo = haz_clases()
//     }
// }
int main(){
    //
    int M;
    M = 1000;
    vector<int> personas;
    int n_personas =100;
    int interacciones = 1000;
    int n_clases = 5 ;
    int rango = (M/28)/n_clases;
    int momentos = 5;
    //vector<int> distribucion_uniforme1 = distribucion_uniforme(personas, M, n_personas);
    vector<int> distribucion_delta1 = distribucion_delta(personas, M, n_personas);
    
    vector<int> intercambio_entre_personas = intercambio(distribucion_delta1,interacciones,n_personas);
    sort(intercambio_entre_personas.begin(),intercambio_entre_personas.end(),ord);

    vector<clase> clases;
    for(int i = 0; i < n_clases; i++){
        clase nueva;
        nueva.min = i*rango;
        nueva.max = (i+1)*(rango);
        nueva.np = 0;
        clases.push_back(nueva);
    }
    vector<clase> c1 = haz_clases(intercambio_entre_personas,clases);

    cout << endl;


    vector<int> aux = intercambio_entre_personas;


    for(int i = 0; i < momentos; i++){
    vector<int> int2 = intercambio(aux,interacciones,n_personas);
    sort(int2.begin(),int2.end(),ord);
    vector<clase> c2 = haz_clases(int2,clases);
    aux = int2;
    cout << endl;
    // entropia
    long long int entropia =0;
    long long int resta = 0;
    for(int k = 0; k < n_clases;k++){
        long long int abc = (long long int) log(clases[k].np);
        resta += clases[k].np*abc;
    }
    long long int bca = (long long int) log(n_personas);
    entropia = n_personas*bca - resta;
    cout << abs(entropia) << endl;
    }
}