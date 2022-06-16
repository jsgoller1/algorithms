/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <set>
using std::set;

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode*>* A_nodes = new set<ListNode*>();
        while(headA != nullptr) {
            A_nodes->insert(headA);
            headA = headA->next;
        }
        
        ListNode* retval = nullptr;
        while(headB != nullptr) {
            if (A_nodes->find(headB) != A_nodes->end()){
                retval = headB;
                break;
            }
            headB = headB->next;
        }
        delete A_nodes;
        return retval;        
    }
};
