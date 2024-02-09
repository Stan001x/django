function analogue1AdjustedTechnicalCondition(){
const analogue1AdjustedDiscount1 = document.querySelector("input[name='analogue1-analogueAdjustedDiscount']");
const analogue1TechnicalConditionAdjustment1 = document.querySelector("input[name='analogue1-analogueTechnicalConditionAdjustment']");
const analogue1AdjustedTechnicalCondition = document.querySelector("#id_analogue1-analogueAdjustedTechnicalCondition");
const analogue1AveragePrice = document.querySelector("#id_analogue1-analogueAveragePrice");
analogue1AdjustedTechnicalCondition.value = `${(parseFloat(analogue1AdjustedDiscount1.value) * parseFloat(analogue1TechnicalConditionAdjustment1.value)).toFixed(2)}`;
analogue1AveragePrice.value = `${((parseFloat(analogue1AdjustedDiscount1.value) * parseFloat(analogue1TechnicalConditionAdjustment1.value)) / 3).toFixed(2)}`;
};


function analogue2AdjustedTechnicalCondition(){
const analogue2AdjustedDiscount2 = document.querySelector("input[name='analogue2-analogueAdjustedDiscount']");
const analogue2TechnicalConditionAdjustment2 = document.querySelector("input[name='analogue2-analogueTechnicalConditionAdjustment']");
const analogue2AdjustedTechnicalCondition = document.querySelector("#id_analogue2-analogueAdjustedTechnicalCondition");
const analogue2AveragePrice = document.querySelector("#id_analogue2-analogueAveragePrice");
analogue2AdjustedTechnicalCondition.value = `${(parseFloat(analogue2AdjustedDiscount2.value) * parseFloat(analogue2TechnicalConditionAdjustment2.value)).toFixed(2)}`;
analogue2AveragePrice.value = `${((parseFloat(analogue2AdjustedDiscount2.value) * parseFloat(analogue2TechnicalConditionAdjustment2.value)) / 3).toFixed(2)}`;
};

function analogue3AdjustedTechnicalCondition(){
const analogue3AdjustedDiscount3 = document.querySelector("input[name='analogue3-analogueAdjustedDiscount']");
const analogue3TechnicalConditionAdjustment3 = document.querySelector("input[name='analogue3-analogueTechnicalConditionAdjustment']");
const analogue3AdjustedTechnicalCondition = document.querySelector("#id_analogue3-analogueAdjustedTechnicalCondition");
const analogue3AveragePrice = document.querySelector("#id_analogue3-analogueAveragePrice");
analogue3AdjustedTechnicalCondition.value = `${(parseFloat(analogue3AdjustedDiscount3.value) * parseFloat(analogue3TechnicalConditionAdjustment3.value)).toFixed(2)}`;
analogue3AveragePrice.value = `${((parseFloat(analogue3AdjustedDiscount3.value) * parseFloat(analogue3TechnicalConditionAdjustment3.value)) / 3).toFixed(2)}`;
};

function objectTotalCost(){
const analogue1AdjustedTechnicalCondition1 = document.querySelector("input[name='analogue1-analogueAdjustedTechnicalCondition']");
const analogue2AdjustedTechnicalCondition2 = document.querySelector("input[name='analogue2-analogueAdjustedTechnicalCondition']");
const analogue3AdjustedTechnicalCondition3 = document.querySelector("input[name='analogue3-analogueAdjustedTechnicalCondition']");
if ((analogue1AdjustedTechnicalCondition1.value > 0) && (analogue2AdjustedTechnicalCondition2.value > 0) && (analogue1AdjustedTechnicalCondition1.value > 0)){
document.querySelectorAll("#id_objectTotalCost").forEach(function(element){
element.value = `${((parseFloat(analogue1AdjustedTechnicalCondition1.value) + parseFloat(analogue2AdjustedTechnicalCondition2.value) + parseFloat(analogue3AdjustedTechnicalCondition3.value)) / 3).toFixed(0) }`
});};

};


document.addEventListener('DOMContentLoaded', function(){

// Корректировка стоимости аналогов или размера скидки на торг

//Выбор стоимости аналога
const analogue1Cost = document.querySelector("input[name='analogue1-analogueCost']");
const analogue2Cost = document.querySelector("input[name='analogue2-analogueCost']");
const analogue3Cost = document.querySelector("input[name='analogue3-analogueCost']");

//Выбор размера скидки на торг
const analogue1Discount = document.querySelector("input[name='analogue1-analogueDiscount']");
const analogue2Discount = document.querySelector("input[name='analogue2-analogueDiscount']");
const analogue3Discount = document.querySelector("input[name='analogue3-analogueDiscount']");


//Выбор ячейки результата корректировки
const analogue1AdjustedDiscount = document.querySelector("#id_analogue1-analogueAdjustedDiscount");
const analogue2AdjustedDiscount = document.querySelector("#id_analogue2-analogueAdjustedDiscount");
const analogue3AdjustedDiscount = document.querySelector("#id_analogue3-analogueAdjustedDiscount");


//Вычисление стоимости после применения корректировки на торг
analogue1Cost.addEventListener("change", (event) => {
analogue1AdjustedDiscount.value = `${(parseFloat(event.target.value) * ((100 + parseFloat(analogue1Discount.value)) / 100) ).toFixed(2)}`;
analogue1AdjustedTechnicalCondition();
objectTotalCost();});

analogue1Discount.addEventListener("change", (event) => {
analogue1AdjustedDiscount.value = `${(parseFloat(analogue1Cost.value) * ((100 + parseFloat(event.target.value)) / 100)).toFixed(2)}`;
analogue1AdjustedTechnicalCondition();
objectTotalCost();});


analogue2Cost.addEventListener("change", (event) => {
analogue2AdjustedDiscount.value = `${(parseFloat(event.target.value) * ((100 + parseFloat(analogue2Discount.value)) / 100) ).toFixed(2)}`;
analogue2AdjustedTechnicalCondition();
objectTotalCost();});

analogue2Discount.addEventListener("change", (event) => {
analogue2AdjustedDiscount.value = `${(parseFloat(analogue2Cost.value) * ((100 + parseFloat(event.target.value)) / 100)).toFixed(2)}`;
analogue2AdjustedTechnicalCondition();
objectTotalCost();});


analogue3Cost.addEventListener("change", (event) => {
analogue3AdjustedDiscount.value = `${(parseFloat(event.target.value) * ((100 + parseFloat(analogue3Discount.value)) / 100) ).toFixed(2)}`;
analogue3AdjustedTechnicalCondition();
objectTotalCost();});

analogue3Discount.addEventListener("change", (event) => {
analogue3AdjustedDiscount.value = `${(parseFloat(analogue3Cost.value) * ((100 + parseFloat(event.target.value)) / 100)).toFixed(2)}`;
analogue3AdjustedTechnicalCondition();
objectTotalCost();});




// Корректировка на физический износ

//Выбор износа аналога
const analogue1Deterioration = document.querySelector("input[name='analogue1-analogueDeterioration']");
const analogue2Deterioration = document.querySelector("input[name='analogue2-analogueDeterioration']");
const analogue3Deterioration = document.querySelector("input[name='analogue3-analogueDeterioration']");

//Выбор износа объекта оценки
const objectPhysicalDeterioration = document.querySelector("input[name='physicalDeterioration']");


//Выбор ячейки результата корректировки
const analogue1TechnicalConditionAdjustment = document.querySelector("#id_analogue1-analogueTechnicalConditionAdjustment");
const analogue2TechnicalConditionAdjustment = document.querySelector("#id_analogue2-analogueTechnicalConditionAdjustment");
const analogue3TechnicalConditionAdjustment = document.querySelector("#id_analogue3-analogueTechnicalConditionAdjustment");


//Вычисление размера корректировки на физический износ
analogue1Deterioration.addEventListener("change", (event) => {
analogue1TechnicalConditionAdjustment.value = `${((1 - objectPhysicalDeterioration.value/100)/(1 - event.target.value/100)).toFixed(4)}`;
analogue1AdjustedTechnicalCondition();
objectTotalCost();});

analogue2Deterioration.addEventListener("change", (event) => {
analogue2TechnicalConditionAdjustment.value = `${((1 - objectPhysicalDeterioration.value/100)/(1 - event.target.value/100)).toFixed(4)}`;
analogue2AdjustedTechnicalCondition();
objectTotalCost();});

analogue3Deterioration.addEventListener("change", (event) => {
analogue3TechnicalConditionAdjustment.value = `${((1 - objectPhysicalDeterioration.value/100)/(1 - event.target.value/100)).toFixed(4)}`;
analogue3AdjustedTechnicalCondition();
objectTotalCost();});

objectPhysicalDeterioration.addEventListener("change", (event) => {
analogue1TechnicalConditionAdjustment.value = `${((1 - event.target.value/100)/(1 - analogue1Deterioration.value/100)).toFixed(4)}`;
analogue1AdjustedTechnicalCondition();
objectTotalCost();
analogue2TechnicalConditionAdjustment.value = `${((1 - event.target.value/100)/(1 - analogue2Deterioration.value/100)).toFixed(4)}`;
analogue2AdjustedTechnicalCondition();
objectTotalCost();
analogue3TechnicalConditionAdjustment.value = `${((1 - event.target.value/100)/(1 - analogue3Deterioration.value/100)).toFixed(4)}`;
analogue3AdjustedTechnicalCondition();
objectTotalCost();
});




/*
// Вычисление скорректированной стоимости после применения корректировки на физическое состояние

//Выбор стоимости аналога
const analogue1AdjustedDiscount1 = document.querySelector("input[name='analogue1-analogueAdjustedDiscount']");
const analogue2AdjustedDiscount1 = document.querySelector("input[name='analogue2-analogueAdjustedDiscount']");
const analogue3AdjustedDiscount1 = document.querySelector("input[name='analogue3-analogueAdjustedDiscount']");

//Выбор размера корректировки на физическое состояние
const analogue1TechnicalConditionAdjustment1 = document.querySelector("input[name='analogue1-analogueTechnicalConditionAdjustment']");
const analogue2TechnicalConditionAdjustment2 = document.querySelector("input[name='analogue1-analogueTechnicalConditionAdjustment']");
const analogue3TechnicalConditionAdjustment3 = document.querySelector("input[name='analogue1-analogueTechnicalConditionAdjustment']");


//Выбор ячейки результата корректировки
const analogue1AdjustedTechnicalCondition = document.querySelector("#id_analogue1-analogueAdjustedTechnicalCondition");
const analogue1AveragePrice = document.querySelector("#id_analogue1-analogueAveragePrice");

const analogue2AdjustedTechnicalCondition = document.querySelector("#id_analogue2-analogueAdjustedTechnicalCondition");
const analogue2AveragePrice = document.querySelector("#id_analogue2-analogueAveragePrice");

const analogue3AdjustedTechnicalCondition = document.querySelector("#id_analogue3-analogueAdjustedTechnicalCondition");
const analogue3AveragePrice = document.querySelector("#id_analogue3-analogueAveragePrice");



//Вычисление стоимости после применения корректировки на физическое состояние
function analogue1AdjustedTechnicalCondition(){
const analogue1AdjustedDiscount1 = document.querySelector("input[name='analogue1-analogueAdjustedDiscount']");
const analogue1TechnicalConditionAdjustment1 = document.querySelector("input[name='analogue1-analogueTechnicalConditionAdjustment']");
analogue1AdjustedTechnicalCondition.value = ((parseFloat(analogue1AdjustedDiscount1.value) * parseFloat(analogue1TechnicalConditionAdjustment1.value)).toFixed(2));
};

analogue1AdjustedDiscount1.addEventListener("change", (event) => {
analogue1AdjustedTechnicalCondition.value = `${(parseFloat(event.target.value) * parseFloat(analogue1TechnicalConditionAdjustment1.value) ).toFixed(2)}`;});

analogue1TechnicalConditionAdjustment1.addEventListener("change", (event) => {
analogue1AdjustedTechnicalCondition.value = `${(parseFloat(analogue1AdjustedDiscount1.value) * parseFloat(event.target.value)).toFixed(2)}`;});


analogue2Cost.addEventListener("change", (event) => {
analogue2AdjustedDiscount.value = `${(parseFloat(event.target.value) * ((100 + parseFloat(analogue2Discount.value)) / 100) ).toFixed(2)}`;});

analogue2Discount.addEventListener("change", (event) => {
analogue2AdjustedDiscount.value = `${(parseFloat(analogue2Cost.value) * ((100 + parseFloat(event.target.value)) / 100)).toFixed(2)}`;});


analogue3Cost.addEventListener("change", (event) => {
analogue3AdjustedDiscount.value = `${(parseFloat(event.target.value) * ((100 + parseFloat(analogue3Discount.value)) / 100) ).toFixed(2)}`;});

analogue3Discount.addEventListener("change", (event) => {
analogue3AdjustedDiscount.value = `${(parseFloat(analogue3Cost.value) * ((100 + parseFloat(event.target.value)) / 100)).toFixed(2)}`;});*/


/*
const analogue1Condition = document.querySelector("input[name='analogue1-analogueDeterioration']");

const resultAnalogue1Condition = document.querySelector("#id_analogue1-analogueTechnicalConditionAdjustment");



const objectCondition = document.querySelector("input[name='physicalDeterioration']");

const analogue1Condition = document.querySelector("input[name='analogue1-analogueDeterioration']");

const resultAnalogue1Condition = document.querySelector("#id_analogue1-analogueTechnicalConditionAdjustment");




 objectCondition.addEventListener("change", (event) => {
  resultAnalogue1Condition.value = `${((1 - event.target.value/100)/(1 - analogue1Condition.value/100)).toFixed(4)}`;});

 analogue1Condition.addEventListener("change", (event) => {
  resultAnalogue1Condition.value = `${((1 - objectCondition.value/100)/(1 - event.target.value/100)).toFixed(4)}`;
  console.log(analogue1Condition.value);});*/




});