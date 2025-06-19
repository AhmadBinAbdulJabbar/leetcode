class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int count = 0;
        for(int i = 0; i < operations.size(); i++){
            if(operations[i][1] == '+'){
                count += 1;
            } else if (operations[i][1] == '-'){
                count -= 1;
            }
        }
        return count;
    }
};