# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

[[Your answer goes here!]]
1.1 Everything works great until you create a pizza order, then, it gives you this error: TypeError: 'topping' is an invalid keyword argument for PizzaTopping. I changed the for loop in line 79 to for topping in toppings_list:
        pizza.toppings.append(PizzaTopping(topping_type=topping))

1.2 In line 82, it was missing the db.session.commit()
1.3 Line 66 to 70, I changed the request.form.get() to order_name and pizza_size


## Exercise 2

1.1 [[Your answer goes here!]]
It works fine until I submit the weather, then it throws me an error: Internal Server Error, and on the back end  File "app.py", line 52, in results
    'city': result_json['name'],
KeyError: 'name'. This is because there's an error with the API

1.2 Also in line 39 and 40, I changed the request.args.get() to city and units
1.3 On line 54, I changed to result_json['main']['temp'], 

## Exercise 3

[[Your answer goes here!]]
1.1 The first error I solved is the index out of range in line 37. I replaced the i with a j

1.2 Then, I got an error in line 51  and 55 
TypeError: list indices must be integers or slices, not float. I added a int(mid) to both