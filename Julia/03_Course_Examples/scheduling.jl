using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x[1:3, 1:4] >= 0)

c = [
    4 4 5 7;
    6 7 5 6;
    12 10 8 11
]

@objective(model, Min, 
    sum(c[i,j] * x[i,j] for i in 1:3, j in 1:4))

production_min = [3000, 6000, 2000]

@constraint(model, [i in 1:3], 
    sum(x[i,j] for j in 1:4) >= production_min[i])

time_limit = [1500, 1200, 1500, 2000]
    
a = [
    0.3 0.25 0.2 0.2;
    0.2 0.3 0.2 0.25;
    0.8 0.6 0.6 0.5
]
@constraint(model, [j in 1:4], sum(a[i,j] * x[i,j] for i in 1:3) <= time_limit[j])


optimize!(model)

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    println("Minimum cost = ", objective_value(model))

    for i in 1:3
        for j in 1:4
            println("Product $i on Machine $j = ", value(x[i,j]))
        end
    end
end
