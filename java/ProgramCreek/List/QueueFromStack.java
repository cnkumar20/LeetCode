package ProgramCreek.List;

import java.util.Stack;

/**
 * Created by dexter on 11/9/16.
 */
public class QueueFromStack {
    Stack<Integer> temp = new Stack<Integer>();
    Stack<Integer> value = new Stack<Integer>();

    public void pop() {
        value.pop();
    }

    public int peek() {
        return value.peek();
    }

    public void push(int a) {
        if(value.isEmpty()) {
            value.push(a);
        }
        else {
            while(!value.isEmpty()) {
                temp.push(value.pop());
            }
            value.push(a);
            while(!temp.isEmpty()) {
                value.push(temp.pop());
            }

        }
    }
}
