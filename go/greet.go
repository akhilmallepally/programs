package main

import "fmt"

func main(){
    const greet string
    greet = "Hi, How are you doing"
    fmt.Println(greet)

    var good string
    fmt.Scan(&good)
    fmt.Printf("I am %v ", good)
}