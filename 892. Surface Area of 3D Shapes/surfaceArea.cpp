class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        // 1. initialization
        int sum_cubes = 0;
        int sum_cubes_surface = 0;
        int sum_overlap = 0;

        // 2. find total surfaces without overlapping
        for (auto row : grid) {
            for (auto entry : row) {
                sum_cubes += entry;
            }
        }
        sum_cubes_surface = sum_cubes * 6;

        // 3. same stack overlapping
        for (auto row : grid) {
            for (auto entry : row) {
                if (entry >= 2)
                    sum_overlap += 2 * (entry - 1);
            }
        }

         // 4. same row overlapping
        for (auto row : grid) {
            for (auto it = row.begin(); it != row.end(); it++) {
                if (it + 1 != row.end()) {
                    sum_overlap += (*it <= *(it + 1))? 2 * (*it) : 2 * (*(it + 1));
                }
            }
        }

        // 5. same column overlapping
        for (int i = 0; i < grid.size() - 1; i++) {// iterate from 0 row to N - 1 row
            for (auto it = grid[i].begin(), it2 = grid[i + 1].begin(); it != grid[i].end(); it++) {
                sum_overlap += (*it <= *(it2))? 2 * (*it) : 2 * (*it2);
                it2++;
            }
        }
        return sum_cubes_surface - sum_overlap ;
    }
};
