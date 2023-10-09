class CalcService:
  def calculate(self, data):

    # データ初期化
    monthlyWeeks = 4.35
    annualMonths = 12
    annualWeeks  = monthlyWeeks * annualMonths
    workDays     = data.get('workDays')
    workHours    = data.get('workHours')
    toolTerm     = data.get('toolTerm')
    toolDays     = data.get('toolDays')
    toolHours    = data.get('toolHours')
    initialCost  = data.get('initialCost')
    runningCost  = data.get('runningCost')
    income       = data.get('income')
    productivity = data.get('productivity') / 100

    # 計算ロジック
    monthlyWorkDays   = monthlyWeeks * workDays
    annualWorkDays    = annualMonths * monthlyWorkDays
    hourlyWage        = income / annualWorkDays / workHours
    dailySavedMinutes = toolHours * productivity * 60
    dailyProfit       = hourlyWage * dailySavedMinutes / 60
    savedTime         = toolHours * productivity * toolDays * annualWeeks * toolTerm
    profit            = savedTime * hourlyWage
    totalCost         = initialCost + runningCost * toolTerm
    roi               = (profit / totalCost) * 100
    paybackDays       = totalCost / (hourlyWage * productivity * toolHours)

    # リターン
    result = {
      "toolTerm"          : int(toolTerm),
      "workHours"         : int(workHours),
      "monthlyWorkDays"   : int(monthlyWorkDays),
      "annualWorkDays"    : int(annualWorkDays),
      "hourlyWage"        : int(hourlyWage),
      "dailySavedMinutes" : int(dailySavedMinutes),
      "dailyProfit"       : int(dailyProfit),
      "savedTime"         : int(savedTime),
      "profit"            : int(profit),
      "totalCost"         : int(totalCost),
      "roi"               : int(roi),
      "paybackDays"       : int(paybackDays)
    }

    return result