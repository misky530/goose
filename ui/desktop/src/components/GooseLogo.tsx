import { SAMYOU_WORDMARK_DATA_URI } from './icons/SamyouWordmark';
import { cn } from '../utils';

interface GooseLogoProps {
  className?: string;
  size?: 'default' | 'small';
  hover?: boolean;
}

// Brand logo for 三友智能助手. Keeps the original GooseLogo API so existing
// callers do not change; the goose SVG + rain hover effect are replaced by
// the SAMYOU wordmark (wide lockup, contained in the original square frame).
export default function GooseLogo({
  className = '',
  size = 'default',
}: GooseLogoProps) {
  const frame = size === 'small' ? 'w-8 h-8' : 'w-16 h-16';

  return (
    <div className={cn(className, frame, 'relative overflow-hidden')}>
      <img
        src={SAMYOU_WORDMARK_DATA_URI}
        alt="SAMYOU"
        className="absolute inset-0 m-auto max-h-full max-w-full object-contain"
      />
    </div>
  );
}
