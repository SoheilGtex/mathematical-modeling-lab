using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x >= 0) # Cheese
@variable(model, y >= 0) # Milk
@variable(model, z >= 0) # Eggs

@objective(model, Min, 100*x + 50*y + 40*z)

@constraint(model, x + 4*y + 2*z >= 12) # Vitamin A
@constraint(model, x + 2*y + 3*z >= 14) # Vitamin B


optimize!(model)

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    println("Cheese = ", value(x))
    println("Milk = ", value(y))
    println("Eggs = ", value(z))
    println("Minimum cost = ", objective_value(model))
else
    println("The model is not solved or not feasible.")
end


