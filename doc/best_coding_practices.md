# Best Coding Practices
When you are writing software always keep in mind maintainability, dependency, efficiency and usability of your code.

## Naming conventions

Using a consistent and descriptive variable and file naming is important. When developers use variables such as a, b, X1 or X2 and do not replace them with a meaningful once, causing confusion and make the code less readable.
Let's make something clear before we move forward.
One of the best naming conventions based on PEP8 can be found at https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html.

Their main points are:
1. General
Avoid using names that are too general or too wordy. Strike a good balance between the two.
2. Packages
Package names should be all lower case
When multiple words are needed, an underscore should separate them
It is usually preferable to stick to 1 word names
3. Modules
Module names should be all lower case
When multiple words are needed, an underscore should separate them
It is usually preferable to stick to 1 word names
4. Classes
Class names should follow the UpperCaseCamelCase convention
Python’s built-in classes, however are typically lowercase words
Exception classes should end in “Error”
5. Global (module-level) Variables
Global variables should be all lowercase
Words in a global variable name should be separated by an underscore
6. Instance Variables
Instance variable names should be all lower case
Words in an instance variable name should be separated by an underscore
Non-public instance variables should begin with a single underscore
If an instance name needs to be mangled, two underscores may begin its name
7. Methods
Method names should be all lowercase
Words in an method name should be separated by an underscore
Non-public method should begin with a single underscore
If a method name needs to be mangled, two underscores may begin its name
8. Method Arguments
Instance methods should have their first argument named ‘self’.
Class methods should have their first argument named ‘cls’
9. Functions
Function names should be all lower case
Words in a function name should be separated by an underscore
10. Constants
Constant names must be fully capitalized
Words in a constant name should be separated by an underscore

## Limit line length
Long lines are hard to read. It is a good practice to avoid writing horizontally long lines of code.

## Avoid Absolute path
It is very bad practice to use absolute path in your code. In general, a path to a file or directory points to a specific location in a file system. When we are using an absolute path we are pointing to a specific location in a file system regardless of current working directory.  Normally working directory refers to a working directory of a process from which it is running.
For example your program requires a file. If you use an absolute path such as  

       original_image = cv2.imread('D:\\ImageManipulation\\beginner_programming\\images\\Color_Image_new.jpg')

When you share your code with someone or you move your code from D drive to C drive. If you run the same code, you will get the error since your application can not find the image to read it. Let's say you run the code and you get an error and fix the path for reading the image but you forget to modify another path for saving the file. After running the code you will get another error because the system can not find the “'D:\\ImageManipulation\\beginner_programming\\images” folder. Imagine if you have many lines of code , changing the path one by one is error prone. You can miss many locations. 
For that reason you should never use absolute paths. Instead use relative paths. 
A relative path is a path which starts from working directory.
Let say application starts from “D:\\ImageManipulation\\beginner_programming\\” then your code will be:

       original_image = cv2.imread('.\\images\\Color_Image_new.jpg')
       cv2.imwrite('.\\images\\gray_Image.jpg', gray_scale_image)
 
Another option is to specify a path in the configuration file.

       output_path = ".\\images\output\\"
       input_path = ".\\images\input\\"
 
        import os
        full_path = os.path.join(config.output_path , ‘Color_Image.jpg”


## Do not Hard Code value
Don't hard code variables in a method instead pass it as an argument. 
For example avoid this:

       def resized(image):       
            image_size = [350,200]
            
Instead the following is more flexible:
       
       def resized(image, image_size):

## Code Reuse: Put common code within a function
Function has an important role in having a clean and manageable code. We can start with a simple idea but as time passes you can find your code is growing and quickly things become harder to manage.  The solution is to store a piece of code that does a single task inside a defined block, and then call that code whenever you need it.
Here are few issues you will face when you do not use function: 
1. When you change your logic you need to change it every place, you have a lot of coupling
2. It is easy to forget to correct all the places so your code can be buggy

## File and folder structure
Function is a great way to reusing your code in Python. Module is another way to reuse the code by organizing similar functions and package them as a file. 

You should avoid writing all of your code in 1-2 files. That won’t break your application but it would be a nightmare to read, debug and maintain later.
Keeping a clean folder structure will make the code a lot more readable and maintainable.

For more information please refer to 
https://github.com/ShiNik/ImageManipulation/tree/master/beginner_programming
https://github.com/ShiNik/ImageManipulation/tree/master/best_practice_programming

## Code readability
Code must be understandable by the other person who did not write the code. Ideally each line of code must be self explanatory. Avoid making the code unnecessarily complex.

## Adding comment but avoid Obvious Comments
Commenting your code is fantastic; however, it can be overdone or just be plain redundant. 
 
For example:

       Example number 1 does not require a comment since it is obvious 
       rectangle_area= width*height
 
       Example number 2 is not obvious and needs a comment
       # Convert milliseconds to seconds
       Time = T * 1000



