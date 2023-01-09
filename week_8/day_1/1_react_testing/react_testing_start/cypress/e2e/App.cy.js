describe('App', ()=>{
    beforeEach(() => {
        cy.visit('http://localhost:3000')

    })
    it("Loads the app", ()=>{
        const counter = cy.get('#counter');
        counter.should('contain', '0')
    })

    it("Add the number", () =>{
        const buttonUp = cy.get('#button-up');
        buttonUp.click();
        const counter = cy.get('#counter');
        counter.should('contain', '1');
    })

    it("Deduct the number", () =>{
        const buttonDown = cy.get('#button-down');
        buttonDown.click();
        const counter = cy.get('#counter');
        counter.should('contain', '-1')
    })

})