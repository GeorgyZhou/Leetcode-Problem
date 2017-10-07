class MyQueue {
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        if (rs.empty()) {
            front = x;
        }
        rs.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int res = peek();
        if (queue.empty()) {
            while (!rs.empty()) {
                queue.push(rs.top());
                rs.pop();
            }
        }
        queue.pop();
        return res;
    }
    
    /** Get the front element. */
    int peek() {
        return queue.empty() ? front : queue.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return rs.empty() && queue.empty();
    }
private:
    stack<int> rs;
    stack<int> queue;
    int front;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * bool param_4 = obj.empty();
 */