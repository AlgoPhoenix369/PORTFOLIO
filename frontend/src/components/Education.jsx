import { useState, useEffect } from 'react';
import { GraduationCap, BookOpen, Clock } from 'lucide-react';

const Education = () => {
  const [visibleItems, setVisibleItems] = useState([]);

  useEffect(() => {
    // Animate items on mount
    const timer = setTimeout(() => {
      setVisibleItems([0, 1, 2]);
    }, 300);
    return () => clearTimeout(timer);
  }, []);

  const education = [
    { 
      degree: 'PhD in Computational Linguistics & AI', 
      school: 'University of Edinburgh', 
      location: 'UK', 
      period: '2018 - 2024',
      description: 'Doctoral research in computational linguistics and artificial intelligence',
      icon: '🎓',
      color: 'from-blue-500 to-cyan-500'
    },
    { 
      degree: 'MSc in Data Science & Machine Learning', 
      school: 'Stanford University', 
      location: 'USA', 
      period: '2015 - 2017',
      description: "Master's degree focusing on machine learning and data science",
      icon: '📊',
      color: 'from-purple-500 to-pink-500'
    },
    { 
      degree: 'BA in Communications & Linguistics', 
      school: "King's College London", 
      location: 'UK', 
      period: '2010 - 2014',
      description: "Bachelor's degree in communications and linguistics",
      icon: '📚',
      color: 'from-emerald-500 to-teal-500'
    },
    { 
      degree: 'Full Stack Software Development', 
      school: 'Moringa School (Kenya)', 
      location: 'Kenya/Remote', 
      period: '2022',
      description: 'Intensive bootcamp in full stack web development',
      icon: '💻',
      color: 'from-amber-500 to-orange-500'
    },
    { 
      degree: 'Certificate in Computer Science', 
      school: 'Harvard College (Online)', 
      location: 'USA', 
      period: '2020',
      description: 'CS50 - Introduction to Computer Science',
      icon: '🏆',
      color: 'from-indigo-500 to-purple-500'
    },
  ];

  return (
    <section id="education" className="section-padding relative overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-slate-900/80 via-blue-900/20 to-slate-900/80"></div>
      <div className="absolute top-0 left-0 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl"></div>
      <div className="absolute bottom-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full filter blur-3xl"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <Clock size={16} className="text-purple-400" />
            <span className="text-sm font-medium text-gray-300">Academic Journey</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Education History</span>
          </h2>
        </div>

        {/* Timeline */}
        <div className="max-w-5xl mx-auto relative">
          {/* Timeline Line */}
          <div className="absolute left-1/2 transform -translate-x-1/2 w-1 h-full bg-gradient-to-b from-blue-500 via-purple-500 to-pink-500 rounded-full"></div>

          {education.map((edu, index) => (
            <div 
              key={index}
              className={`relative flex items-center mb-12 transition-all duration-1000 ${
                visibleItems.includes(index) 
                  ? 'opacity-100 translate-x-0' 
                  : 'opacity-0 translate-x-20'
              }`}
              style={{ transitionDelay: `${index * 200}ms` }}
            >
              {/* Timeline Dot */}
              <div className={`absolute left-1/2 transform -translate-x-1/2 w-8 h-8 bg-gradient-to-r ${edu.color} rounded-full border-4 border-slate-900 shadow-lg z-10 animate-pulse`}></div>
              
              {/* Content - Alternating Sides */}
              <div className={`w-1/2 ${index % 2 === 0 ? 'pr-16' : 'ml-auto pl-16'}`}>
                <div className="glass-card p-8 rounded-3xl card-hover group relative overflow-hidden">
                  {/* Gradient Background on Hover */}
                  <div className={`absolute inset-0 bg-gradient-to-r ${edu.color} opacity-0 group-hover:opacity-10 transition-opacity duration-500`}></div>
                  
                  <div className="relative">
                    {/* Icon */}
                    <div className="text-5xl mb-4 transform group-hover:scale-110 transition-transform duration-300">
                      {edu.icon}
                    </div>
                    
                    {/* Degree */}
                    <h3 className="text-xl font-bold text-white mb-2 group-hover:gradient-text transition-all duration-300">
                      {edu.degree}
                    </h3>
                    
                    {/* School */}
                    <p className={`text-lg font-semibold bg-gradient-to-r ${edu.color} bg-clip-text text-transparent mb-3`}>
                      {edu.school}
                    </p>
                    
                    {/* Meta */}
                    <div className="flex items-center justify-between text-sm text-gray-400 mb-4 pb-4 border-b border-white/10">
                      <span className="flex items-center space-x-2">
                        <BookOpen size={14} />
                        <span>{edu.location}</span>
                      </span>
                      <span className="font-mono bg-white/10 px-3 py-1 rounded-full">{edu.period}</span>
                    </div>
                    
                    {/* Description */}
                    <p className="text-gray-300 text-sm leading-relaxed">
                      {edu.description}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Education;
