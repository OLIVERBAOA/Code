#include <iostream>
#include <cstdio>

using namespace std;

bool foo(string st){
    int len = st.length();
    if(len < 3) return false;
    for(int i = len / 3; i > 0; --i){//枚举M的长度
        if(st.substr(0, i) != st.substr(len - i - 1, i)) continue;
        for(int j = i; j <= len -  2 * i; ++j){//在i到 len - i - 1中看是否有M
            cout << i << "," << j << endl;
            cout << st.substr(0, i) << "," << st.substr(j, i) << endl;
            if(st.substr(0, i) == st.substr(j, i)){
                cout << st.substr(0, i) << endl;
                return true;
            }
        }
    }    
    return false;
}

int main(){
    int t;
    cin >> t;
    while(t--){
        string st;
        cin >> st;
        if(!foo(st)) 
            cout << "Naive Music" << endl;
    }
    return 0;
}
