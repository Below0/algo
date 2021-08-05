#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int maze[1005][1005];
int visit[1005][1005];
int trap_check[1005];
int N;
int MIN = 300001;
int START, END;

typedef struct {
    int node, n;
}P;

int solution(int n, int start, int end, vector<vector<int> > roads, vector<int> traps){
    vector<int>::iterator iter;
    int ts, te, tn, tnode, is_trap=0, i, target, result = 0;
    START = start; END = end; N = n;
    P tp;
    queue<P> q;
    P p = {0, 0};
    q.push(p);
    fill(&visit[0][0], &visit[n - 1][n], MIN);
    
    for(vector<vector<int> >::iterator it=roads.begin(); it != roads.end(); it++){
        ts = (*it)[0] - 1; te = (*it)[1] - 1; tn = (*it)[2];
        printf("%d %d %d\n", ts, te, tn);
        maze[ts][te] = tn;
    }
    
    for(iter=traps.begin(); iter !=traps.end(); iter++){
        trap_check[(*iter) - 1] = 1;
    }
    
    while(!q.empty()){
        tp = q.front();
        q.pop();
        tnode = tp.node; tn = tp.n;
        is_trap = trap_check[tnode];
        if(tnode == 0) printf("status: %d is_trap: %d n=%d MIN=%d\n",tnode, is_trap, tn, MIN);
        
        if(tp.node+1 == END){
            if(tn < MIN) MIN = tn;
            result = MIN;
            continue;
        }
        
        for(i = 0; i < N; i++){
            if(is_trap == 1) target = maze[i][tp.node]; // trap일 경우 반대
            else {
                trap_check[tnode] *= -1;
                target = maze[tp.node][i];
            }
            
            if(target && tn + target < visit[tnode][i]){

                if(tnode == 1) printf("\t target=%d , %d %d\n", target, visit[tnode][i], tn + target);
                P tp = {i,tn+target};
                visit[tnode][i] = tn + target;
                if(tnode == 1) printf("\t %d\n",visit[tnode][i]);
                
                q.push(tp);
            }
        }
    
    }
    
    return result;
    
}

int main(){
    vector<vector<int> > v;
    vector<int> a, b, c, t;
    a.push_back(1);a.push_back(2);a.push_back(1);
    b.push_back(3);b.push_back(2);b.push_back(1);
    c.push_back(2);c.push_back(4);c.push_back(1);
    t.push_back(2);t.push_back(3);
    v.push_back(a);
    v.push_back(b);
    printf("%d\n",solution(4, 1, 4, v, t));
    
    
    return 0;
}
