
/*In this program we will know how to use assign a constant and a variable. Variable can be assigned in different ways. We will explore the other way in next examples.

And don't worry about other syntax. Just ignore as of now.
*/

package main

import "fmt"

func main(){
    const greet = "Hi, How are you doing"
    fmt.Println(greet)

    var good string
    fmt.Scan(&good)
    fmt.Printf("I am doing %v ", good)
}