using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x[1:5] >= 0) # Regular time
@variable(model, y[1:5] >= 0) # Overtime
@variable(model, z[1:4] >= 0) # Ending inventory

@objective(model, Min, 
    10*(x[1]+x[2]+x[3]+x[4]+x[5]) + 15*(y[1]+y[2]+y[3]+y[4]+y[5]) + 2*(z[1]+z[2]+z[3]+z[4]))

@constraint(model, x[1] + y[1] - z[1] == 1200)
@constraint(model, x[2] + y[2] + z[1] - z[2] == 2100)
@constraint(model, x[3] + y[3] + z[2] - z[3] == 2400)
@constraint(model, x[4] + y[4] + z[3] - z[4] == 3000)
@constraint(model, x[5] + y[5] + z[4] == 4000)


optimize!(model)

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    println("Minimum cost: ", objective_value(model))

    for t in 1:5
        println("Month $t: Regular = ", value(x[t]),
                ", Overtime = ", value(y[t]))
        if t <= 4
            println("  Ending inventory = ", value(z[t]))
        end
    end
end