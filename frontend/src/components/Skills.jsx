import { Code, Database, Server, Settings, Brain, Zap } from 'lucide-react';

const Skills = () => {
  const skillCategories = [
    {
      icon: <Code size={32} />,
      title: 'Languages & Frameworks',
      color: 'from-blue-500 to-cyan-500',
      glow: 'glow',
      skills: [
        { name: 'Python', level: 95 },
        { name: 'JavaScript', level: 85 },
        { name: 'TensorFlow', level: 88 },
        { name: 'PyTorch', level: 85 },
        { name: 'Transformers', level: 90 },
      ],
    },
    {
      icon: <Brain size={32} />,
      title: 'AI & Data Training',
      color: 'from-purple-500 to-pink-500',
      glow: 'glow-purple',
      skills: [
        { name: 'RLHF', level: 95 },
        { name: 'LLM Fine-tuning', level: 90 },
        { name: 'Data Annotation', level: 95 },
        { name: 'Prompt Engineering', level: 92 },
        { name: 'Model Evaluation', level: 90 },
      ],
    },
    {
      icon: <Server size={32} />,
      title: 'DevOps & Cloud',
      color: 'from-green-500 to-emerald-500',
      glow: 'glow',
      skills: [
        { name: 'AWS', level: 88 },
        { name: 'Google Cloud', level: 85 },
        { name: 'Docker', level: 85 },
        { name: 'Git', level: 90 },
        { name: 'CI/CD', level: 82 },
      ],
    },
    {
      icon: <Settings size={32} />,
      title: 'Tools & Platforms',
      color: 'from-orange-500 to-red-500',
      glow: 'glow-pink',
      skills: [
        { name: 'Label Studio', level: 90 },
        { name: 'Snorkel', level: 87 },
        { name: 'Weights & Biases', level: 85 },
        { name: 'Jupyter', level: 95 },
        { name: 'VS Code', level: 92 },
      ],
    },
  ];

  return (
    <section id="skills" className="section-padding relative overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 dot-pattern opacity-20"></div>
      <div className="absolute top-0 left-0 w-96 h-96 bg-purple-500/10 rounded-full filter blur-3xl"></div>
      <div className="absolute bottom-0 right-0 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <Zap size={16} className="text-yellow-400" />
            <span className="text-sm font-medium text-gray-300">Expertise</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Technical Skills</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            A comprehensive toolkit for AI training and machine learning
          </p>
        </div>

        {/* Skills Grid */}
        <div className="grid md:grid-cols-2 gap-8">
          {skillCategories.map((category, index) => (
            <div key={index} className="group relative">
              {/* Glow Effect */}
              <div className={`absolute -inset-1 bg-gradient-to-r ${category.color} rounded-3xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500 ${category.glow}`}></div>
              
              {/* Card */}
              <div className="relative glass-card rounded-3xl overflow-hidden card-hover">
                {/* Header */}
                <div className={`bg-gradient-to-r ${category.color} p-8`}>
                  <div className="flex items-center space-x-4">
                    <div className="p-4 bg-white/20 rounded-2xl backdrop-blur-sm text-white">
                      {category.icon}
                    </div>
                    <h3 className="text-2xl font-black text-white">{category.title}</h3>
                  </div>
                </div>

                {/* Skills List */}
                <div className="p-8 space-y-5">
                  {category.skills.map((skill, skillIndex) => (
                    <div key={skillIndex} className="group/skill">
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
                          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent shimmer"></div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Additional Skills Tags */}
        <div className="mt-16 text-center">
          <h3 className="text-2xl font-bold mb-8 text-white">Core Competencies</h3>
          <div className="flex flex-wrap justify-center gap-4">
            {[
              'NLP', 'Machine Learning', 'Deep Learning', 'Computer Vision',
              'Data Analysis', 'Statistical Modeling', 'Research', 'Technical Writing',
              'Team Leadership', 'Mentoring', 'Remote Collaboration', 'Agile',
            ].map((skill, index) => (
              <div
                key={index}
                className="px-6 py-3 glass rounded-full text-gray-300 hover:text-white card-hover cursor-default border border-white/10 hover:border-white/30"
              >
                {skill}
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Skills;
