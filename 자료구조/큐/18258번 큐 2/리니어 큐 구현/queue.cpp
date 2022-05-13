#include <iostream>
#include <string>
using namespace std;

class Queue{
    public:
        Queue(int std_size);
        Queue(const Queue &queue);

        ~Queue();

        void push(int n);
        int pop();
        int get_size() const { return size; }
        bool is_empty() const { return size == 0; }
        int get_front() const ;
        int get_back() const ;

    private:
        void double_array_size();
        int* queue_array;
        int size;
        int max_size;
};

Queue::Queue(int std_size) {
    queue_array = new int[std_size];
    size = 0;
    max_size = std_size;
}

Queue::Queue(const Queue &queue) {
    queue_array = new int[queue.max_size];
    for (int i = 0; i < queue.size; i++)
    {
        queue_array[i] = queue.queue_array[i];
    }
    size = queue.size;
    max_size = queue.max_size;
}

Queue::~Queue() {
    delete[] queue_array;
    queue_array = nullptr;
}

void Queue::double_array_size() {
    max_size *= 2;
    int* new_queue_array = new int[max_size];
    
    for (int i = 0; i < size; i++)
    {
        new_queue_array[i] = queue_array[i];
    }

    delete[] queue_array;
    queue_array = new_queue_array;
    new_queue_array = nullptr;
}

void Queue::push(int n) {
    if (size < max_size)
    {
        queue_array[size++] = n;
        return;
    }

    double_array_size();
    queue_array[size++] = n;
}

int Queue::pop() {
    if (size == 0)
    {
        return -1;
    }
    
    int return_value = queue_array[0];
    for (int i = 0; i < size; i++)
    {
        queue_array[i] = queue_array[i + 1];
    }
    size--;
    max_size--;
    return return_value;
}

int Queue::get_front() const {
    if (size == 0)
    {
        return -1;
    }

    return queue_array[0];
}

int Queue::get_back() const {
    if (size == 0) {
        return -1;
    }

    return queue_array[size - 1];
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int command_num;
    cin >> command_num;

    Queue queue = Queue(command_num);
    for (int i = 0; i < command_num; i++)
    {
        string command_tkn;
        cin >> command_tkn;

        if (command_tkn.compare("push") == 0)
        {
            int push_num;
            cin >> push_num;

            queue.push(push_num);
        } else if (command_tkn.compare("pop") == 0)
        {
            cout << queue.pop() << "\n";
        } else if (command_tkn.compare("size") == 0)
        {
            cout << queue.get_size() << "\n";
        } else if (command_tkn.compare("empty") == 0)
        {
            if (queue.is_empty())
            {
                cout << 1 << "\n";
            } else
            {
                cout << 0 << "\n";
            }
            
        } else if (command_tkn.compare("front") == 0)
        {
            cout << queue.get_front() << "\n";
        } else if (command_tkn.compare("back") == 0)
        {
            cout << queue.get_back() << "\n";
        }
    }
    
    return 0;
}
