describe('Comments', () =>{
    beforeEach(() =>{
        cy.visit('http://localhost:3000')
    })

    it('Contains comments', () =>{
        const commentList = cy.get('#comment-list > li');
        commentList.should('have.length', 2)

    })

    it("Add comments", () =>{
        const nameInput = cy.get('#name-input').type('Larry')
        const commentInput = cy.get('#comment-input').type('Done!!')
        // cy.get('#comment-form').submit()
        cy.get('input[value="Post"]').click()
        cy.get('#comment-list').should('contain', 'Larry').should('contain', 'Done!!')        
    })
})