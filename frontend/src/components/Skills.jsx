import { useState, useEffect } from 'react';
import { Code, Database, Server, Settings, Brain, Zap, Filter, ChevronRight } from 'lucide-react';

const Skills = () => {
  const [activeCategory, setActiveCategory] = useState('all');
  const [visibleSkills, setVisibleSkills] = useState([]);

  const skillCategories = [
    {
      id: 'languages',
      icon: <Code size={24} />,
      title: 'Languages & Frameworks',
      color: 'from-blue-400 to-cyan-400',
      glow: 'shadow-blue-500/50',
      skills: [
        { name: 'Python', level: 95 },
        { name: 'JavaScript', level: 85 },
        { name: 'TensorFlow', level: 88 },
        { name: 'PyTorch', level: 85 },
        { name: 'Transformers', level: 90 },
        { name: 'Scikit-learn', level: 90 },
        { name: 'Pandas', level: 92 },
        { name: 'NumPy', level: 90 },
      ],
    },
    {
      id: 'ai',
      icon: <Brain size={24} />,
      title: 'AI & Data Training',
      color: 'from-purple-400 to-pink-400',
      glow: 'shadow-purple-500/50',
      skills: [
        { name: 'RLHF', level: 95 },
        { name: 'LLM Fine-tuning', level: 90 },
        { name: 'Data Annotation', level: 95 },
        { name: 'Prompt Engineering', level: 92 },
        { name: 'Model Evaluation', level: 90 },
        { name: 'NLP', level: 88 },
        { name: 'Computer Vision', level: 82 },
      ],
    },
    {
      id: 'devops',
      icon: <Server size={24} />,
      title: 'DevOps & Cloud',
      color: 'from-emerald-400 to-teal-400',
      glow: 'shadow-emerald-500/50',
      skills: [
        { name: 'AWS', level: 88 },
        { name: 'Google Cloud', level: 85 },
        { name: 'Docker', level: 85 },
        { name: 'Git', level: 90 },
        { name: 'CI/CD', level: 82 },
        { name: 'Kubernetes', level: 78 },
      ],
    },
    {
      id: 'tools',
      icon: <Settings size={24} />,
      title: 'Tools & Platforms',
      color: 'from-amber-400 to-orange-400',
      glow: 'shadow-amber-500/50',
      skills: [
        { name: 'Label Studio', level: 90 },
        { name: 'Snorkel', level: 87 },
        { name: 'Weights & Biases', level: 85 },
        { name: 'Jupyter', level: 95 },
        { name: 'VS Code', level: 92 },
        { name: 'MLflow', level: 83 },
      ],
    },
  ];

  const filteredCategories = activeCategory === 'all' 
    ? skillCategories 
    : skillCategories.filter(cat => cat.id === activeCategory);

  useEffect(() => {
    // Animate skills on category change
    const timer = setTimeout(() => {
      setVisibleSkills(filteredCategories.map(() => true));
    }, 100);
    return () => clearTimeout(timer);
  }, [activeCategory]);

  return (
    <section id="skills" className="section-padding relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/5 via-purple-500/5 to-pink-500/5"></div>
      
      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <Zap size={16} className="text-yellow-400" />
            <span className="text-sm font-medium">Expertise</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Technical Skills</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            A comprehensive toolkit for AI training and machine learning
          </p>
        </div>

        {/* Filter Buttons with Slide Animation */}
        <div className="flex flex-wrap justify-center gap-4 mb-12">
          <button
            onClick={() => setActiveCategory('all')}
            className={`px-6 py-3 rounded-xl font-semibold transition-all duration-500 flex items-center space-x-2 transform hover:scale-105 ${
              activeCategory === 'all'
                ? 'bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 text-white shadow-lg shadow-purple-500/50 scale-105'
                : 'glass text-gray-400 hover:text-white hover:bg-white/10'
            }`}
          >
            <Filter size={18} />
            <span>All</span>
          </button>
          {skillCategories.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setActiveCategory(cat.id)}
              className={`px-6 py-3 rounded-xl font-semibold transition-all duration-500 flex items-center space-x-2 transform hover:scale-105 ${
                activeCategory === cat.id
                  ? `bg-gradient-to-r ${cat.color} text-white shadow-lg ${cat.glow} scale-105`
                  : 'glass text-gray-400 hover:text-white hover:bg-white/10'
              }`}
            >
              {cat.icon}
              <span className="hidden sm:inline">{cat.title.split(' ')[0]}</span>
            </button>
          ))}
        </div>

        {/* Skills Grid with Slide Transitions */}
        <div className="grid md:grid-cols-2 gap-8">
          {filteredCategories.map((category, catIndex) => (
            <div 
              key={catIndex} 
              className={`group relative transition-all duration-700 transform ${
                visibleSkills[catIndex] 
                  ? 'opacity-100 translate-x-0' 
                  : 'opacity-0 translate-x-20'
              }`}
              style={{ transitionDelay: `${catIndex * 150}ms` }}
            >
              {/* Glow Effect */}
              <div className={`absolute -inset-1 bg-gradient-to-r ${category.color} rounded-3xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500 shadow-2xl`}></div>
              
              {/* Card */}
              <div className="relative glass-card rounded-3xl overflow-hidden card-hover">
                {/* Header */}
                <div className={`bg-gradient-to-r ${category.color} p-6`}>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-4">
                      <div className="p-3 bg-white/20 rounded-xl backdrop-blur-sm text-white">
                        {category.icon}
                      </div>
                      <h3 className="text-xl font-black text-white">{category.title}</h3>
                    </div>
                    <ChevronRight size={24} className="text-white/50 group-hover:translate-x-2 transition-transform duration-300" />
                  </div>
                </div>

                {/* Skills List with Staggered Animation */}
                <div className="p-6 space-y-4">
                  {category.skills.map((skill, skillIndex) => (
                    <div 
                      key={skillIndex} 
                      className="group/skill"
                      style={{ animationDelay: `${skillIndex * 50}ms` }}
                    >
                      <div className="flex justify-between mb-2">
                        <span className="text-gray-300 font-medium group-hover/skill:text-white transition-colors duration-300">
                          {skill.name}
                        </span>
                        <span className="text-gray-400 text-sm font-mono">{skill.level}%</span>
                      </div>
                      <div className="relative h-3 bg-slate-700/50 rounded-full overflow-hidden">
                        <div 
                          className={`absolute inset-y-0 left-0 h-full bg-gradient-to-r ${category.color} rounded-full transition-all duration-1000 ease-out`}
                          style={{ width: `${skill.level}%` }}
                        >
                          {/* Shimmer Effect */}
                          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-shimmer"></div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Skill Level Legend */}
        <div className="mt-16 glass-card p-8 rounded-2xl max-w-3xl mx-auto">
          <h3 className="text-xl font-bold text-white mb-6 text-center">Proficiency Levels</h3>
          <div className="grid grid-cols-3 gap-6">
            {[
              { range: '90-100%', label: 'Expert', color: 'from-emerald-400 to-green-400', desc: 'Deep expertise' },
              { range: '75-89%', label: 'Advanced', color: 'from-blue-400 to-cyan-400', desc: 'Strong proficiency' },
              { range: '60-74%', label: 'Intermediate', color: 'from-purple-400 to-pink-400', desc: 'Working knowledge' },
            ].map((item, index) => (
              <div key={index} className="text-center group cursor-default">
                <div className={`inline-block px-4 py-2 bg-gradient-to-r ${item.color} rounded-full text-white font-bold text-sm mb-2 transform group-hover:scale-110 transition-transform duration-300`}>
                  {item.range}
                </div>
                <div className="text-white font-semibold mb-1">{item.label}</div>
                <div className="text-gray-400 text-sm">{item.desc}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Skills;
