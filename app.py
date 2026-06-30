from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bmi(height_cm, weight_kg):
    """計算 BMI"""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def bmi_status(bmi):
    """判斷 BMI 狀態"""
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "正常範圍"
    elif bmi < 27:
        return "過重"
    elif bmi < 30:
        return "輕度肥胖"
    elif bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"


def blood_pressure_status(systolic, diastolic):
    """判斷血壓狀態"""
    if systolic >= 180 or diastolic >= 120:
        return "高血壓危象，建議立即就醫"
    elif systolic >= 140 or diastolic >= 90:
        return "第二期高血壓"
    elif (130 <= systolic < 140) or (80 <= diastolic < 90):
        return "第一期高血壓"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "血壓偏高"
    elif systolic < 120 and diastolic < 80:
        return "血壓正常"
    else:
        return "請確認輸入數值是否正確"


@app.route("/", methods=["GET", "POST"])
def index():
    bmi_result = None
    bp_result = None

    if request.method == "POST":
        form_type = request.form.get("form_type")

        try:
            if form_type == "bmi":
                height = float(request.form.get("height"))
                weight = float(request.form.get("weight"))

                if height <= 0 or weight <= 0:
                    bmi_result = "請輸入大於 0 的身高與體重"
                else:
                    bmi = calculate_bmi(height, weight)
                    status = bmi_status(bmi)
                    bmi_result = f"你的 BMI 為 {bmi}，判斷結果：{status}"

            elif form_type == "bp":
                systolic = int(request.form.get("systolic"))
                diastolic = int(request.form.get("diastolic"))

                if systolic <= 0 or diastolic <= 0:
                    bp_result = "請輸入大於 0 的血壓數值"
                else:
                    status = blood_pressure_status(systolic, diastolic)
                    bp_result = f"你的血壓為 {systolic}/{diastolic} mmHg，判斷結果：{status}"

        except ValueError:
            if form_type == "bmi":
                bmi_result = "請輸入正確的數字"
            elif form_type == "bp":
                bp_result = "請輸入正確的數字"

    return render_template("index.html", bmi_result=bmi_result, bp_result=bp_result)


if __name__ == "__main__":
    app.run(debug=True)
