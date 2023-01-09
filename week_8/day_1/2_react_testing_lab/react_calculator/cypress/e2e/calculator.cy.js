describe("Calculator", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000");
  })

  it('should have working number buttons', () => {
    cy.get('#number2').click();
    cy.get('.display').should('contain', 2)
  })

  it('arithmetical operations should update the display', () =>{
    cy.get('#number2').click();
    cy.get('#operator-multiply').click();
    cy.get('#number4').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', 8)
  })

  it('multiple operations should be able to chained together', () =>{
    cy.get('#number2').click();
    cy.get('#operator-multiply').click();
    cy.get('#number4').click();
    cy.get('#operator-multiply').click();
    cy.get('#number2').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', 16)
  })

  it('Output should be expected for a range of numbers', () =>{
    //Multiply large number
    cy.get('#number2').click();
    for (let i = 0;i < 4;i++){
      cy.get('#number0').click();
    }
    cy.get('#operator-multiply').click();
    cy.get('#number4').click();
    for (let i = 0;i < 4;i++){
      cy.get('#number0').click();
    }
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', 800000000)
    // Divide positive
    cy.get('#operator-divide').click();
    cy.get('#number1').click();
    for (let i = 0;i < 8;i++){
      cy.get('#number0').click();
    }
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', 8)
    // Subtract negative
    cy.get('#operator-subtract').click();
    cy.get('#number9').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', -1)
    // Divide decimal
    cy.get('#operator-divide').click();
    cy.get('#number3').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', -0.333)
  })

  it('should shown not a number', () =>{
    cy.get('#number4').click();
    cy.get('#operator-divide').click();
    cy.get('#number0').click();
    cy.get('#operator-equals').click();
    cy.get('.display').should('contain', 'Not a Number')
  })
})