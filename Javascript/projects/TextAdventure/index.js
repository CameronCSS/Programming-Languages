const prompt = require("prompt-sync")();

const answer = prompt("Would you like to play (y/n)? ")

if (answer === "y") {
    game()
}
else {
    console.log("That's too bad");
}

function game(){
while(true){
if (answer.toLowerCase() === "y") {
    console.clear();
    let a = prompt("Would you like to go left or right (left/right) ? ");

    if (a === "left") {
        // left
        console.clear();
        console.log("You go left and fall in a sewer");
        console.log("");
        console.log("You die covered in shit");
        console.log("");
        break
    } else {
        // right
        console.clear();
        console.log("NICE. You see a hot lady.");
        console.log("");
        let a = prompt("Would you like to follow her (y/n) ? ");
        if (a === "y") {
            // follow her
            console.clear();
            console.log("She pulls out a gun and shoots you");
            console.log("");
            console.log("YOU DIED");
            console.log("");
            break
        } else {
            // dont follow her
            console.clear();
            console.log("Woah look at that Ferrari.");
            console.log("");
            a = prompt("Want to get in it (y/n) ? ");
        }
        if (a === "y") {
            // got in car
            console.clear();
            console.log("This is a sweet ride.");
            console.log("Is that a bag of coke? like... cocaine??");
            console.log("");
            a = prompt("Want to do cocaine (y/n) ? ");
            if (a === "y"){
                console.clear();
                console.log("This is your first time doing cocaine.");
                console.log("");
                console.log("You Overdose and YOU DIE");
                console.log("");
                break
            }else {
                console.clear();
                console.log("You dont see anything obvious.");
                console.log("");
                a = prompt("Want to check the glove box (y/n) ? ");
            }  if (a === "y"){
                console.clear();
                console.log("Is that ANOTHER bag of coke?");
                console.log("");
                a = prompt("Want to do cocaine (y/n) ? ");
            } if (a === "y"){
                console.clear();
                console.log("This is your first time doing cocaine.");
                console.log("");
                console.log("You OD and YOU DIE");
                console.log("");
                break
            } else{
                console.clear();
                console.log("You get out of the car cause you are lame.");
                console.log("");
                a = prompt("Want to see if you can catch up to that lady (y/n) ? ");
            }  if (a === "y"){
                console.clear();
                console.log("You start yelling after her and begin to follow her");
                console.log("She starts running.");
                console.log("");
                a = prompt("Do you want to give chase (y/n) ? ");
                if (a === "y"){
                    console.clear();
                    console.log("You start running after her");
                    console.log("She pulls out her gun and points it at you");
                    console.log("");
                    a = prompt("Want to back off (y/n) ? ");
                    if (a === "y"){
                        console.clear();
                        console.log("You back off");
                        console.log("You accidentally step into the street and get hit by a bus");
                        console.log("");
                        console.log("YOU DIED!");
                        console.log("");
                        break
                    } else{
                        console.clear();
                        console.log("You slowly approach her");
                        console.log("She points her gun and shoots you");
                        console.log("");
                        console.log("YOU DIED!");
                        console.log("");
                        break
                    }
                }
            } else {
                console.clear();
                console.log("You see a $100 bill on the ground");
                console.log("");
                a = prompt("want to pick it up (y/n) ? ");
            } if (a === "y"){
                console.clear();
                console.log("You begin to reach for the $100 bill");
                console.log("You feel something poke your back and a man demand your wallet");
                console.log("");
                a = prompt("want to give it to him (y/n) ? ");
                if (a === "y"){
                    console.clear();
                    console.log("You're a pussy");
                    console.log("He takes your wallet and then shoots you.");
                    console.log("");
                    console.log("YOU DIED!");
                    console.log("");
                        break
                } else {
                    console.clear();
                    console.log("He takes your wallet anyways and then shoots you.");
                    console.log("");
                    console.log("YOU DIED!");
                    console.log("");
                    break
                }
            } else {
                console.clear();
                console.log("You feel something poke your back and a man demand your wallet");
                console.log("");
                a = prompt("want to give it to him (y/n) ? ");
            } if (a === "n"){
                console.clear();
                console.log("You whip around like an action star and grab his gun");
                console.log("Now he is on the ground begging for his life");
                console.log("");
                a = prompt("Want to shoot him (y/n) ? ");
                if (a === "y"){
                    console.clear();
                    console.log("You shoot him");
                    console.log("a bunch of people tackle you and try to take the gun away.");
                    console.log("");
                    a = prompt("Should you start blasting (y/n) ? ");
                    if (a === "y") {
                        console.clear();
                        console.log("The police pull up and shoot you");
                        console.log("Several people got shot by you. And then you got shot by the police");
                        console.log("");
                        console.log("YOU DIED!");
                        console.log("");
                        break
                    } else {      
                        console.clear();                   
                        console.log("The police pull up and arrest you");
                        console.log("You are now serving several life sentences");
                        console.log("");
                        a = prompt("Should you try and join a prison gang (y/n) ? ");
                        if (a === "y") {
                            console.clear();
                            a = prompt("Want to join the Aryan Brotherhood (y/n)? ");
                            if (a === "y"){
                                console.clear();
                                console.log("In the next prison riot you fight alongside the Aryan Brotherhood");
                                console.log("You guys lose and you are forced to do sexual favors for the biggest dude in prison");
                                console.log("");
                                console.log("He stretches you out to the point of death. YOU DIED!!");
                                console.log("");
                                break
                            } else{
                                console.clear();
                                a = prompt("Want to join the Black Guerilla Family (BGF) (y/n)? ");
                                if (a === "y"){
                                    console.clear();
                                    console.log("In the next prison riot you fight alongside the BGF");
                                    console.log("You guys lose and you are forced to do sexual favors for the biggest dude in prison");
                                    console.log("");
                                    console.log("He stretches you out to the point of death. YOU DIED!!");
                                    console.log("");
                                    break
                                }
                                else{
                                    console.clear();
                                    a = prompt("Want to join the Mexican Mafia (y/n)? ");
                                    if (a === "y"){
                                        console.clear();
                                        console.log("In the next prison riot you fight alongside the Mexican Mafia");
                                        console.log("You guys lose and you are forced to do sexual favors for the biggest dude in prison");
                                        console.log("");
                                        console.log("He stretches you out to the point of death. YOU DIED!!");
                                        console.log("");
                                        break
                                    }
                                    else {
                                        console.clear();
                                        console.log("You decide to stay away from the gangs.");
                                        console.log("While out in the yard you spot the biggest dude in prison");
                                        console.log("");
                                        a = prompt("Want to approach him (y/n)? ");
                                    }
                                    if (a === "y"){
                                        console.clear();
                                        console.log("You slowly walk towards the biggest dude in prison");
                                        console.log("Everyone in the yard is looking at you");
                                        console.log("");
                                        a = prompt("Still want to approach him (y/n)? ");
                                    } else{
                                        console.clear();
                                        console.log("You decide this was a stupid idea");
                                        console.log("You turn around and start to walk away");
                                        console.log("");
                                        console.log("You get shivved in the back and YOU DIED!!!");
                                        console.log("");
                                        break
                                    }
                                    if (a === "y"){
                                        console.clear();
                                        console.log("You finally get up to the big guy");
                                        console.log("He just stares at you");
                                        console.log("");
                                        console.log("You get shivved in the back and YOU DIED!!!");
                                        console.log("");
                                        break
                                    }
                                    else {
                                        console.clear();
                                        console.log("You finally make good choices");
                                        console.log("You lay low and get out on good behavior");
                                        console.log("");
                                        a = prompt("Want to go back to your family (y/n)? ");
                                    }
                                    if (a === "y"){
                                        console.clear();
                                        console.log("They take you back like nothing ever happened");
                                        console.log("You live a long happy life");
                                        console.log("");
                                        console.log("CONGRATULATIONS YOU WON!!!");
                                        console.log("");
                                        break
                                    } else{
                                        console.clear();
                                        console.log("You become homeless and have to give BJs for money");
                                        console.log("You get a dog to keep you company");
                                        console.log("He dies in the winter");
                                        console.log("");
                                        console.log("You get sick and DIE a few days later");
                                        console.log("");
                                        break
                                    }

                            
                        }
                    }
                }
                
                else {
                    console.clear();
                    console.log("You're a pussy");
                    console.log("You get killed by a random dude");
                    console.log("");
                    console.log("YOU DIED!");
                    console.log("");
                    break
                }
            }
        } else {
            // didnt get in the car
            console.clear();
            console.log("You're a pussy");
            console.log("A random man comes by and mugs you because you are weak");
            console.log("");
            let a = prompt("Want to fight back (y/n) ? ");
            if (a === "y") {
                // fought back
                console.clear();
                console.log("You try to fight back. But you are sooo weak.");
                console.log("He pushes you over and you hit your head");
                console.log("");
                console.log("You bleed out while crying. YOU DIED!!");
                console.log("");
                break
            } else {
                // let him mug you
                console.clear();
                console.log("You didnt even fight back cause you are sooo weak.");
                console.log("He pushes you over and you hit your head");
                console.log("");
                console.log("You bleed out while crying. YOU DIED!!");
                console.log("");
                break
            }
        }
    }else{
        console.clear();
        console.log("You're a pussy");
        console.log("He takes your wallet and then shoots you.");
        console.log("");
        console.log("YOU DIED!");
        console.log("");
            break
    }
} else {
    console.clear();
    console.log("You keep walking and see a cat");
    console.log("He distracts you from the construction worker moving a big beam");
    console.log("");
    console.log("You get your head smashed and YOU DIE!");
    console.log("");
    break
}
}
}
else {
    console.log("Tha's too bad");
    break
}
}
const again = prompt("Would you like to play again (y/n)? ")
if (again === "y") {
    game()
}
else {
    console.log("That's too bad");
}
}
