# Definition for singly-linked list.
#class ListNode(object):
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next

class Solution(object):
    def spiralMatrix(self,m,n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        matrix = self.generateMatrix(m,n)
        #i need to know how to index into a sublist
        #matrix [0][0] = 1
        #return matrix
        h = len(head)
        #return h
        #return len(matrix)
        i = 0
        j = 0
        directions = ["right", "down", "left", "up"]
        d = 0
        count = 0

        while count <= h-1:
            print (directions[d])
            
            if matrix [i][j] == -1 :
                if directions[d] == "right":
                    matrix[i][j] = head[count]
                    count += 1
                    if j < n-1:
                        j += 1
                    else:
                        i += 1
                        d = (d + 1) % len(directions)
            
                elif directions[d] == "down":
                    matrix[i][j] = head[count]
                    count += 1
                    if i < m-1:
                        i += 1
                    else:
                        j -= 1
                        d = (d + 1) % len(directions)
                
                elif directions[d] == "left":
                    matrix[i][j] = head[count]
                    count += 1
                    if j > 0:
                        j -= 1
                    else:
                        i -= 1
                        d = (d + 1) % len(directions)

                else:
                    matrix[i][j] = head[count]
                    count += 1
                    if i > 0:
                        i -= 1
                    else:
                        j += 1
                        d = (d + 1) % len(directions)
            
            else:
                #we loop through the directions
                d = (d + 1) % len(directions)
                i += 1
                j += 1
                print(matrix)
        
        return matrix

    def generateMatrix(self,m,n):
        matrix = []
        for i in range(m):
            rows = []
            for j in range(n):
                rows.append(-1)
            matrix.append(rows)
        return matrix
    
def main():
    solution = Solution()
    matrix = solution.generateMatrix(3,5)
    print(matrix)
    solution = solution.spiralMatrix(3,5,[3,0,2,6,8,1,7,9,4,2,5,5,0])
    print(solution)
if __name__ == "__main__":
    main()