import React from 'react';

const StoriesTopics = ({storytopic}) =>{

    const stories = storytopic.map((story, index) => {
        return <li key={index}><a href={`${story.url}`}>{story.title}</a></li>
    })



    return (

        <div>
            {stories}
        </div>

    )
    
};

export default StoriesTopics;