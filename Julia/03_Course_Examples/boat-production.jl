using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x >= 0) # Regular boats
@variable(model, y >= 0) # Competition boats

@objective(model, Max, 50*x + 80*y)

@constraint(model, 50*x + 30*y <= 1000) # Aluminum
@constraint(model, 20*x + 15*y <= 300) # Machine time
@constraint(model, 3*x + 5*y <= 200) # Human labor


optimize!(model)

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    println("Regular boats = ", value(x))
    println("Competition boats = ", value(y))
    println("Maximum profit = ", objective_value(model))
else
    println("The model is not solved or not feasible.")
end





