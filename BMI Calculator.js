function CalculateBMI(Weight, Height)
{
    var BMI = (Weight / (Math.pow(Height, 2)));
    return BMI
}

function InterpretBMI() {
    var Weight = prompt("Enter your weight in kg: ");
    var Height = prompt("Enter your height in meters: ");
    var BMI = CalculateBMI(Weight, Height);

    if (BMI < 18.5) {
        if (confirm("BMI = " + BMI + ", You are underweight 😐\nTry again?"))
        {
            InterpretBMI();
        }
    }
    else if (BMI >= 18.5 && BMI < 25) {
        if (confirm("BMI = " + BMI + ", You are normal weight 😊\nTry again?"))
        {
            InterpretBMI();
        }
    }
    else if (BMI >= 25 && BMI < 30) {
        if (confirm("BMI = " + BMI + ", You are overweight 😅\nTry again?"))
        {
            InterpretBMI();
        }
    }
    else if (BMI >= 30 && BMI < 40) {
        if (confirm("BMI = " + BMI + ", You are so obese 😲\nTry again?"))
        {
            InterpretBMI();
        }
    }
}

InterpretBMI();