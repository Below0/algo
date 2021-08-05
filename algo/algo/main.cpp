#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int visit[210] = {0};
int N;


void dfs(int x, vector<int> computers[]){
    visit[x] = 1;
    for(int i = 0; i < N; i++){
        if(x != i && computers[x][i] && !visit[i]) dfs(i, computers);
    }
}

int solution(int n, vector<int> computers[]) {
    N = n;
    int answer = 0;
    
    for(int i = 0; i < n; i++){
        if(!visit[i]){
            dfs(i, computers);
            answer++;
        }
    }
    
    return answer;
}

int main(){
    vector<int> inp[] = {{1,1,0}, {1,1,0}, {0,0,1}};
    printf("%d\n", solution(3, inp));
    
    
    return 0;
}
