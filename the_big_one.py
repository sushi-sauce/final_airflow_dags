from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import Variable

dag= DAG(
         "food_hall", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )

t1 = DummyOperator(
            task_id = 'wash_rice',
            dag = dag,          
    )

t2 = DummyOperator(
            task_id = 'cook_rice',
            dag = dag
    )  
t3 = DummyOperator(
         task_id = 'season_rice',
         dag = dag
    )
t4 = DummyOperator(
            task_id = 'slice_vegetables',
            dag = dag
    )

t5= DummyOperator(
            task_id = 'prepare_fish',
            dag = dag
    )
t6= DummyOperator(
            task_id = 'toast_nori',
            dag = dag
    )

t7= DummyOperator(
            task_id = 'sushi_roll_1',
            dag = dag
    )

t8= DummyOperator(
            task_id = 'prep_chicken',
            dag = dag
    )

t9 = DummyOperator(
            task_id = 'bread_chicken',
            dag = dag
    )
t10 = DummyOperator(
            task_id = 'tempura_chicken',
            dag = dag
    )
t11= DummyOperator(
            task_id = 'prep_crab',
            dag = dag
    )
t12 = DummyOperator(
            task_id = 'boil_water',
            dag = dag
    )
t13 = DummyOperator(
            task_id = 'add_green_tea',
            dag = dag
    )
t14 = DummyOperator(
            task_id = 'sushi_roll_2',
            dag = dag
    )
t15 = DummyOperator(
            task_id = 'sushi_roll_3',
            dag = dag
    )
t16 = DummyOperator(
            task_id = 'bread_shrimp',
            dag = dag
    )
t17 = DummyOperator(
            task_id = 'tempura_shrimp',
            dag = dag
    )

cake_list = Variable.get("cake_list", deserialize_json=True)

t16 = DummyOperator(
            task_id = 'measure_ingredients',
            dag = dag,          
    )

t17 = DummyOperator(
            task_id = 'preheat_oven',
            dag = dag
    )  

t18 = DummyOperator(
            task_id = 'make_frosting',
            dag = dag
    )
t19 = DummyOperator(
            task_id = 'bake_cake',
            dag = dag
    )
t20= DummyOperator(
            task_id = 'finish_cake',
            dag = dag
    )

for element in cake_list:
    t21 = DummyOperator(
         task_id = 'mix_' + str(element)+ '_batter',
         dag = dag
    )
    t16 >> t21 >> t19

t26 = DummyOperator(
            task_id = 'wash_lettuce_',
            dag = dag,          
    )

t27 = DummyOperator(
            task_id = 'slice_tomatoes',
            dag = dag
    )  
t28 = DummyOperator(
         task_id = 'toast_bun',
         dag = dag
    )
t29 = DummyOperator(
            task_id = 'prep_burger_meat',
            dag = dag
    )

t30= DummyOperator(
            task_id = 'cook_burger',
            dag = dag
    )

t31= DummyOperator(
            task_id = 'assemble_burger',
            dag = dag
    )
    
t32= DummyOperator(
            task_id = 'slice_cheese',
            dag = dag
    )
t33= DummyOperator(
            task_id = 'cut_potatoes',
            dag = dag
    )

t34= DummyOperator(
            task_id = 'fry_fries',
            dag = dag
    )

t35= DummyOperator(
            task_id = 'season_fries',
            dag = dag
    )
t36 = DummyOperator(
            task_id = 'season_ground_beef',
            dag = dag,          
    )

t37 = DummyOperator(
            task_id = 'cook_ground_beef',
            dag = dag
    )  
t38 = DummyOperator(
         task_id = 'shred_cheese',
         dag = dag
    )
t39 = DummyOperator(
            task_id = 'shred_lettuce',
            dag = dag
    )

t40= DummyOperator(
            task_id = 'assemble_taco',
            dag = dag
    )

t41= DummyOperator(
            task_id = 'fry_chips',
            dag = dag
    )
t42= DummyOperator(
            task_id = 'prepare_salsa',
            dag = dag
    )
t43= DummyOperator(
            task_id = 'chips_n_salsa',
            dag = dag
    )

t44= DummyOperator(
            task_id = 'prepare_sauce',
            dag = dag
    )

t45= DummyOperator(
            task_id = 'make_corn_tortilla',
            dag = dag
    )
t46= DummyOperator(
            task_id = 'assemble_enchilada',
            dag = dag
    )
t47= DummyOperator(
            task_id = 'wash_lettuce',
            dag = dag
    )

t48 = DummyOperator(
         task_id = 'wash_rice_',
         dag = dag
    )
t49 = DummyOperator(
            task_id = 'cook_rice_',
            dag = dag
    )

t50= DummyOperator(
            task_id = 'kimchi',
            dag = dag
    )
t51= DummyOperator(
            task_id = 'make_sauce_',
            dag = dag
    )
t52= DummyOperator(
            task_id = 'slice_vegetables_',
            dag = dag
    )
t53= DummyOperator(
            task_id = 'fry_egg',
            dag = dag
    )
t54= DummyOperator(
            task_id = 'assemble_bibimbap',
            dag = dag
    )
t55= DummyOperator(
            task_id = 'soak_rice_cakes',
            dag = dag
    )
t56= DummyOperator(
            task_id = 'cook_rice_cakes_in_sauce',
            dag = dag
    )
t57= DummyOperator(
            task_id = 'tteokbokki',
            dag = dag
    )

t58 = DummyOperator(
         task_id = 'soak_rice_noodles',
         dag = dag
    )
t59 = DummyOperator(
            task_id = 'prep_sauce',
            dag = dag
    )
t60= DummyOperator(
            task_id = 'slice_green_onions',
            dag = dag
    )
t61= DummyOperator(
            task_id = 'wash_beansprouts',
            dag = dag
    )
t62= DummyOperator(
            task_id = 'marinate_chicken',
            dag = dag
    )
t63= DummyOperator(
            task_id = 'stir_fry',
            dag = dag
    )
t64= DummyOperator(
            task_id = 'pad_thai',
            dag = dag
    )
t65= DummyOperator(
            task_id = 'make_sauce',
            dag = dag
    )
t66= DummyOperator(
            task_id = 'pick_fresh_thai_basil',
            dag = dag
    )
t67= DummyOperator(
            task_id = 'thai_basil_chicken',
            dag = dag
    )

t58>>t63
t59>>t63
t60>>t63
t61>>t63
t62>>t63
t63>>t64
t65>>t63
t66>>t63
t63>>t67
t48>>t49
t49>>t54
t50>>t54
t51>>t54
t52>>t54
t53>>t54
t51>>t56
t55>>t56
t56>>t57
t36>>t37
t37 >> t46
t44>>t46
t45>>t46
t38>>t46
t38>>t40
t37>>t40
t39>>t40
t47>>t39
t41>>t42>>t43




t26>>t31
t27>>t31
t28>>t31
t29>>t30>>t31
t32>>t31
t33>>t34>>t35
t18 >>t20
t17 >> t19
t19 >>t20
t1 >> t2 >> t3
t4 >>t7
t5 >> t7
t3 >>t7
t6 >> t7
t8 >> t9 >> t10
t12 >> t13
t3>>t14
t11 >>t14
t6>>t14
t6>>t15
t3 >> t15
t16>>t17
t17 >>t15
t4>>t15
