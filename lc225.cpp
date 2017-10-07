class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        if (queue1.empty()) {
            queue2.push(x);
        } else if (queue2.empty()) {
            queue1.push(x);
        }
        surf = x;
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int res;
        if (!queue1.empty()) {
            while (queue1.size() > 1) {
                surf = queue1.front();
                queue2.push(surf);
                queue1.pop();
            }
            res = queue1.front();
            queue1.pop();
        } else if (!queue2.empty()) {
            while (queue2.size() > 1) {
                surf = queue2.front();
                queue1.push(surf);
                queue2.pop();
            }
            res = queue2.front();
            queue2.pop();
        }
        return res;
    }
    
    /** Get the top element. */
    int top() {
        return surf;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return queue1.empty() && queue2.empty();
    }
private:
    queue<int> queue1;
    queue<int> queue2;
    int surf;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */