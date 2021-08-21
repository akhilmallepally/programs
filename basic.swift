import UIKit

let constant = 10
var number = 4
var result = constant + number

var message = "Learning Swift"

message.append("a")
message.uppercased()
message.count


var items = 10
var price = 200
var total = price * items
var invoice = "Total price for purchase of $\(items) items = " + String(total)
//This is same as f{} in python
var invoice1 = "Total price for purchase of $\(items) items = $\(items)"



var emojiDict = ["👻":" Ghost", "😤" : "Angry",  "😱" :"Scream"]
var wordtolook = "😱"
var meaning = emojiDict[wordtolook]

print(meaning)

wordtolook = "😤"
meaning = "Angry"

print(meaning)
