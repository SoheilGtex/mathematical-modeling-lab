using JuMP
using HiGHS


model = Model(HiGHS.Optimizer)

@variable(model, x[1:4] >= 0)
@variable(model, y[1:3] >= 0)

@objective(model, Min,
    20 * (0.07 * x[1] + 0.06 * x[2] + 0.065 * x[3] + 0.075 * x[4]))

@constraint(model, x[1] - y[1] == 2)
@constraint(model, x[2] + 1.06 * y[1] - y[2] == 4)
@constraint(model, x[3] + 1.055 * y[2] - y[3] == 8)
@constraint(model, x[4] + 1.045 * y[3] == 5)



# کد مربوط به «حل مدل» توسط هوش مصنوعی نوشته شده

# Solve the model
optimize!(model)

# Display the results
println("Termination status: ", termination_status(model))

if is_solved_and_feasible(model)
    println("Minimum total interest cost: ", objective_value(model))

    for i in 1:4
        println("Stocks sold in year $i: ", value(x[i]))
    end

    for i in 1:3
        println("Short-term deposit in year $i: ", value(y[i]))
    end
end