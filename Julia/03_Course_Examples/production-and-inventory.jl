import MathOptInterface as MOI
using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, 0 <= x[1:5] <= 2000) # Regular time
@variable(model, 0 <= y[1:5] <= 600) # Overtime
@variable(model, z[1:4] >= 0) # Ending inventory

@objective(model, Min, 
    10*(x[1]+x[2]+x[3]+x[4]+x[5]) + 15*(y[1]+y[2]+y[3]+y[4]+y[5]) + 2*(z[1]+z[2]+z[3]+z[4]))

@constraint(model, x[1] + y[1] - z[1] == 1200)
@constraint(model, x[2] + y[2] + z[1] - z[2] == 2100)
@constraint(model, x[3] + y[3] + z[2] - z[3] == 2400)
@constraint(model, x[4] + y[4] + z[3] - z[4] == 3000)
@constraint(model, x[5] + y[5] + z[4] == 4000)



optimize!(model)

@assert termination_status(model) == MOI.OPTIMAL

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    min_cost = objective_value(model)

    println("Minimum cost: ", min_cost)

    for t in 1:5
        println("Month $t: Regular = ", value(x[t]),
                ", Overtime = ", value(y[t]))

        if t <= 4
            println("  Ending inventory = ", value(z[t]))
        end
    end

    @assert isapprox(
        min_cost,
        152300.0;
        atol=1e-6
    )
else
    error("The model is not solved or not feasible.")
end
