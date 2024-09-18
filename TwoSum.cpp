#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
         for(int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if(map.find(complement) != map.end()){
                return vector<int>{map[complement], i};
            }
            map[nums[i]] = i;
         }  
         return vector<int>{};
    }

int main(){
    
  vector<int> nums = {1,2,3,4};
  int target = 7;
  
  vector<int> res;

  res = twoSum(nums, target);

  cout << res[0] << ", " << res[1] << endl;

  return 0;
}
