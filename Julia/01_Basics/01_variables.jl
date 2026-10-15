
# Variables in Julia
# ==================

# 1. Assigning values to variables
price = 120.0
quantity = 5

# 2. Using variables in calculations
total_cost = price * quantity

# 3. Updating a variable
quantity = 8
total_cost = price * quantity

# 4. Displaying results
println("Price: ", price)
println("Quantity: ", quantity)
println("Total cost: ", total_cost)

# 5. A mathematical modeling example
fixed_cost = 1000.0
unit_cost = 25.0
production_quantity = 40

total_production_cost = fixed_cost + unit_cost * production_quantity

println("Production cost: ", total_production_cost)
