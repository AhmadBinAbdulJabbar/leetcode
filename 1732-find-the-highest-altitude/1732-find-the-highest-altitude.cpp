class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int netGain = 0;
        int maxGain = 0;

        for (int i = 0; i < gain.size(); i++){
            netGain += gain[i];
            if (maxGain < netGain){
                maxGain = netGain;
            } 
        }

        return maxGain;
    }
};