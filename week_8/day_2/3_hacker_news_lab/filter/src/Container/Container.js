import React, { useState, useEffect } from 'react';
import SearchBar from '../components/form';
import StoriesTopics from '../components/StoriesTopics';




function Maincontainer() {
    const [storiesTopic, setStoriesTopic] = useState([])
    const [storiesNo, setStoriesNo] = useState([])
    const [value, setValue] = useState("")
    const [alltopics, setAlltopics] = useState([])    
    const filter = (event) =>{
        setValue(event.target.value)
    }

    useEffect(() =>{
        fetch('https://hacker-news.firebaseio.com/v0/topstories.json')
        .then(res => res.json())
        .then(data => {
            const shortStoriesNo = data.slice(0, 10)
            const topics =  shortStoriesNo.map(topicnumber =>{
                let newurl = `https://hacker-news.firebaseio.com/v0/item/${topicnumber}.json`;
                return fetch(newurl).then(response => response.json());
            })
            setStoriesNo(data)
            Promise.all(topics)
            .then(stories => {
                setStoriesTopic(stories)
                setAlltopics(stories)
                // console.log(data)
            })

        })
    }, [])

    
    const filter123 = () =>{
        // if (!value) { 
        //     setAlltopics(storiesTopic)
        // }else{
            const filtered = alltopics.filter((topic) => topic.title.toLowerCase().includes(value.toLowerCase()));
            setAlltopics(filtered)
            console.log('yes')
            return filtered
        // };

    }

    useEffect(() => {
        filter123()
    }, [value]);
        

    return (
        <div>
            <SearchBar filter={filter} value={value}/>
            <StoriesTopics storytopic={alltopics}/>
        </div>
  );
}

export default Maincontainer;
