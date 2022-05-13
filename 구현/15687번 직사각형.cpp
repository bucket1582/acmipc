class Rectangle{
    Rectangle(int width, int height);

    int width;
    int height;

    int get_width() const { return width; }
    int get_height() const { return height; }
    void set_width(int width) { this->width = width; }
    void set_height(int height) {this->height = height; }
    int area() const { return width * height; }
    int perimeter() const { return 2 * (width + height); }
    bool is_square() const { return width == height; }
};

Rectangle::Rectangle(int width, int height): width(width), height(height) {}