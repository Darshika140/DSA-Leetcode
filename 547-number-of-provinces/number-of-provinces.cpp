class Solution {
public:
void dfs(int city, vector<vector<int>>& adj, vector<bool>& visited)
        {
            visited[city]=true;
            for(int neighbors : adj[city])
            {
                if(!visited[neighbors]){
                    dfs(neighbors, adj, visited);

                }
            }
        }
    int findCircleNum(vector<vector<int>>& isConnected) {
        
        
        int city= isConnected.size();
        vector<vector<int>> adj(city);
        for(int i=0; i<city; i++){
            for(int j=0; j<city; j++){
                if(isConnected[i][j]==1 && i!=j){
                    adj[i].push_back(j);

                }

            }
        }
        vector<bool> visited(city, false);
        int provinces=0;
        for(int i=0; i<city; i++){
            if(!visited[i]){
                dfs(i,adj,visited);
                provinces+=1;
            }
        }
        
        return provinces;


        
    }
};