#include <iostream>

/*
This is the LeetCode official solution. I wasn't sure it would work (it did), so I copied it here for testing.
*/

 //Definition for singly-linked list.
 struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(nullptr) {}
  };

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pA = headA;
        ListNode *pB = headB;
        while (pA != pB) {
            pA = pA == nullptr ? headB : pA->next;
            pB = pB == nullptr ? headA : pB->next;
        }
        return pA;
        // Note: In the case lists do not intersect, the pointers for A and B
        // will still line up in the 2nd iteration, just that here won't be
        // a common node down the list and both will reach their respective ends
        // at the same time. So pA will be NULL in that case.
    }
};

int main(){
    ListNode listA =  ListNode(1);
    ListNode listB =  ListNode(2);
    ListNode listC =  ListNode(3);
    listB.next = &listC;
    Solution s = Solution();
    std::cout << s.getIntersectionNode(&listA, &listB) << std::endl;
    return 0;
}