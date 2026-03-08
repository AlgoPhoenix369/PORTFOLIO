import { ArrowDown, Github, Linkedin, Mail, Sparkles } from 'lucide-react';

const Hero = () => {
  return (
    <section id="home" className="min-h-screen flex items-center justify-center relative overflow-hidden bg-gradient-to-br from-slate-900 via-purple-900/20 to-slate-900">
      {/* Animated Background */}
      <div className="absolute inset-0 overflow-hidden">
        {/* Grid Pattern */}
        <div className="absolute inset-0 grid-pattern opacity-30"></div>
        
        {/* Animated Blobs */}
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-blue-500/30 rounded-full mix-blend-screen filter blur-3xl opacity-70 animate-blob"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-purple-500/30 rounded-full mix-blend-screen filter blur-3xl opacity-70 animate-blob animation-delay-200"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-pink-500/30 rounded-full mix-blend-screen filter blur-3xl opacity-70 animate-blob animation-delay-400"></div>
        
        {/* Floating Particles */}
        {[...Array(20)].map((_, i) => (
          <div
            key={i}
            className="absolute w-1 h-1 bg-white/30 rounded-full float"
            style={{
              top: `${Math.random() * 100}%`,
              left: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 5}s`,
              animationDuration: `${5 + Math.random() * 5}s`,
            }}
          ></div>
        ))}
      </div>

      <div className="container-custom relative z-10 text-center px-6">
        {/* Verified Badge */}
        <div className="animate-fade-in mb-8 inline-flex items-center space-x-2 glass px-6 py-3 rounded-full">
          <Sparkles size={18} className="text-yellow-400" />
          <span className="text-sm font-medium text-gray-300">Available for opportunities</span>
        </div>

        {/* Name with Epic Gradient */}
        <h1 className="text-6xl md:text-8xl lg:text-9xl font-black mb-6 animate-slide-up tracking-tight">
          <span className="gradient-text block">Babajide Salami</span>
        </h1>

        {/* Title with Glow */}
        <div className="relative inline-block mb-8 animate-slide-up animation-delay-200">
          <p className="text-2xl md:text-3xl lg:text-4xl text-gray-300 font-light">
            AI Training Specialist <span className="text-white/40">&</span> Software Engineer
          </p>
          <div className="absolute -inset-4 bg-gradient-to-r from-blue-500/20 via-purple-500/20 to-pink-500/20 blur-2xl -z-10"></div>
        </div>

        {/* Location */}
        <p className="text-gray-400 mb-10 animate-slide-up animation-delay-400 flex items-center justify-center space-x-2">
          <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
          <span>Croydon, England, United Kingdom</span>
        </p>

        {/* Summary */}
        <p className="text-xl text-gray-400 mb-12 max-w-4xl mx-auto leading-relaxed animate-slide-up animation-delay-600">
          Pioneering the future of AI through <span className="text-blue-400 font-semibold">RLHF</span>,{' '}
          <span className="text-purple-400 font-semibold">LLM evaluation</span>, and{' '}
          <span className="text-pink-400 font-semibold">intelligent data annotation</span> for next-generation AI systems.
        </p>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-6 mb-16 animate-slide-up animation-delay-600">
          <a href="#projects" className="btn-primary-custom group">
            <span className="relative z-10 flex items-center">
              View My Work
              <ArrowDown size={20} className="ml-2 group-hover:translate-y-1 transition-transform duration-300" />
            </span>
          </a>
          <a href="#contact" className="btn-secondary-custom group">
            <span className="relative z-10 flex items-center">
              Get In Touch
              <Mail size={20} className="ml-2 group-hover:rotate-12 transition-transform duration-300" />
            </span>
          </a>
        </div>

        {/* Social Links with Glow */}
        <div className="flex items-center justify-center space-x-6 animate-slide-up animation-delay-600">
          {[
            { href: 'https://github.com/PhoenixAlgo369', icon: <Github size={26} />, label: 'GitHub' },
            { href: 'https://linkedin.com/in/babajide-salami-', icon: <Linkedin size={26} />, label: 'LinkedIn' },
            { href: 'mailto:babajide.salami@email.com', icon: <Mail size={26} />, label: 'Email' },
          ].map((social, index) => (
            <a
              key={index}
              href={social.href}
              target="_blank"
              rel="noopener noreferrer"
              className="group flex flex-col items-center space-y-2"
            >
              <div className="p-4 glass rounded-2xl text-gray-400 group-hover:text-white group-hover:glow transition-all duration-300 group-hover:scale-110">
                {social.icon}
              </div>
              <span className="text-xs text-gray-500 group-hover:text-gray-300 transition-colors duration-300">{social.label}</span>
            </a>
          ))}
        </div>

        {/* Scroll Indicator */}
        <div className="absolute bottom-10 left-1/2 transform -translate-x-1/2 animate-bounce">
          <a href="#about" className="flex flex-col items-center space-y-2 text-gray-500 hover:text-white transition-colors duration-300">
            <span className="text-xs uppercase tracking-widest">Scroll</span>
            <ArrowDown size={28} className="text-gray-400" />
          </a>
        </div>
      </div>
    </section>
  );
};

export default Hero;
